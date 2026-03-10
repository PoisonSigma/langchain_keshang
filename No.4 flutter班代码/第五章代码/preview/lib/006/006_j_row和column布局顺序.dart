/*
Row 的布局过程分为六个步骤：
1.对每个非flex 因子的子控件（例如，那些没有被 Expanded 包裹的）进行布局,
2.mainAxis主轴约束是无限大的,crossAxis交叉轴的约束是传入的最大尺寸   使用无限制的水平约束和传入的垂直约束。如果 crossAxisAlignment 是 CrossAxisAlignment.stretch，则使用与传入的最大高度相匹配的紧密垂直约束。
3.根据它们的 flex 因子，将剩余的mainAxis主轴空间按照比例分配给Expanded等控件
4.按照crossAxis交叉轴高度,按照传入的最大高度布局每个子控件.(取所有子控件的最大值进行设置,而不是单独设置每个子控件的高度)
使用与步骤 1 中相同的垂直约束对剩余的每个子控件进行布局，但使用基于步骤 2 中分配的空间量的水平约束，而不是使用无限制的水平约束。具有 Flexible.fit 属性为 FlexFit.tight 的子控件将获得紧密的约束（即，被强制填充分配的空间），而具有 Flexible.fit 属性为 FlexFit.loose 的子控件将获得宽松的约束（即，不被强制填充分配的空间）。
5.Row 的高度是其子控件中的最大高度（这总是满足传入的垂直约束）。
6.Row的宽度是mainAxisSize 决定,如果mainAxisSize = MainAxisSize.min 则宽度是所有子控件宽度的总和
 */
