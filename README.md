# mask_detection

#### 介绍
基于yolov5的口罩检测项目

#### 安装教程

1.  推荐Pycharm作为运行环境
2.  推荐使用anaconda管理python环境
3.  需要pytorch支持

#### 使用说明

1.  main.py为图形界面，请对其进行修改（如果必要），之后运行它。
2.  kid.pt为目前训练的最优模型，在训练次数不足的情况下已有较高的准确率。
3.  识别文件请将图像置于\data\images中

#### 参与贡献

1. Fork 本仓库
2. 新建 Feat_xxx 分支
3. 提交代码
4. 新建 Pull Request

#### If error keep happening, try to modify upsampling.py as follows.
    def forward(self, input: Tensor) -> Tensor:
        # return F.interpolate(input, self.size, self.scale_factor, self.mode, self.align_corners,
        #                      recompute_scale_factor=self.recompute_scale_factor)
        return F.interpolate(input, self.size, self.scale_factor, self.mode, self.align_corners)