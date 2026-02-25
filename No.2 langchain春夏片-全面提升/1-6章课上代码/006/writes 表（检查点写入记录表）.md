检查点数据库表结构的分析

checkpoints表

```
CREATE TABLE checkpoints (
                thread_id TEXT NOT NULL,
                checkpoint_ns TEXT NOT NULL DEFAULT '',
                checkpoint_id TEXT NOT NULL,
                parent_checkpoint_id TEXT,
                type TEXT,
                checkpoint BLOB,
                metadata BLOB,
                PRIMARY KEY (thread_id, checkpoint_ns, checkpoint_id)
            )
```

| 字段名                 | 类型 | 约束                | 含义与作用                                                   |
| ---------------------- | ---- | ------------------- | ------------------------------------------------------------ |
| `thread_id`            | TEXT | NOT NULL            | 线程 / 会话 ID：核心隔离维度，区分不同用户会话、不同任务流（如用户 A 的对话、用户 B 的对话）。 |
| `checkpoint_ns`        | TEXT | NOT NULL DEFAULT '' | 检查点命名空间：用于隔离同一 `thread_id` 下不同场景 / 模块的检查点（如 Agent 检查点、Chain 检查点），避免 ID 冲突。 |
| `checkpoint_id`        | TEXT | NOT NULL            | 检查点唯一 ID：在 `thread_id + checkpoint_ns` 维度下唯一标识一个检查点（如某一步执行的快照 ID）。 |
| `parent_checkpoint_id` | TEXT | 可选                | 父检查点 ID：构建检查点的父子链路（如步骤 1→步骤 2，步骤 2 的父 ID 是步骤 1），支持执行回溯、分支恢复。 |
| `type`                 | TEXT | 可选                | 检查点类型：标识检查点所属的组件类型（如 `agent`/`chain`/`tool`），便于分类解析状态。 |
| `checkpoint`           | BLOB | 可选                | 核心状态数据：序列化后的检查点主体（如 Chain 中间结果、Agent 思考状态、工具调用上下文），BLOB 适配复杂对象（如 Pickle/JSON 二进制）。 |
| `metadata`             | BLOB | 可选                | 元数据：检查点的附加信息（如创建时间、执行时长、用户 ID），非核心但辅助溯源。 |

```
CREATE TABLE writes (
                thread_id TEXT NOT NULL,
                checkpoint_ns TEXT NOT NULL DEFAULT '',
                checkpoint_id TEXT NOT NULL,
                task_id TEXT NOT NULL,
                idx INTEGER NOT NULL,
                channel TEXT NOT NULL,
                type TEXT,
                value BLOB,
                PRIMARY KEY (thread_id, checkpoint_ns, checkpoint_id, task_id, idx)
            )
```

## `writes` 表（检查点写入记录表）

该表存储**检查点执行过程中向指定通道的输出内容**（如 Agent 思考日志、工具响应、用户可见输出），每个记录对应一次具体的写入操作，字段解析如下：

| 字段名          | 类型    | 约束                | 含义与作用                                                   |
| --------------- | ------- | ------------------- | ------------------------------------------------------------ |
| `thread_id`     | TEXT    | NOT NULL            | 关联 `checkpoints` 表的线程 ID，核心关联维度。               |
| `checkpoint_ns` | TEXT    | NOT NULL DEFAULT '' | 关联 `checkpoints` 表的命名空间，保证关联维度一致。          |
| `checkpoint_id` | TEXT    | NOT NULL            | 关联 `checkpoints` 表的检查点 ID，定位写入操作所属的检查点。 |
| `task_id`       | TEXT    | NOT NULL            | 子任务 ID：标识检查点下的具体子任务（如一个 Agent 检查点包含 “调用工具 A”“解析结果” 两个子任务）。 |
| `idx`           | INTEGER | NOT NULL            | 写入索引：同一 `task_id + channel` 下的写入顺序（如一个任务向同一通道写了 3 行内容，idx=0/1/2 区分顺序）。 |
| `channel`       | TEXT    | NOT NULL            | 输出通道：写入的目标通道名称（如 `agent_output`/`tool_response`/`stdout`），区分不同类型的输出。 |
| `type`          | TEXT    | 可选                | 写入值类型：标识 `value` 的数据类型（如 `string`/`json`/`binary`），便于解析。 |
| `value`         | BLOB    | 可选                | 写入内容：序列化后的输出数据（如 Agent 思考文本、工具返回的 JSON 结果），BLOB 适配多类型数据。 |

**主键约束**：`(thread_id, checkpoint_ns, checkpoint_id, task_id, idx)`

## 两表的关联作用

核心关联键：`thread_id + checkpoint_ns + checkpoint_id`（三个字段联合）