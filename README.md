# ur_rtde
## 代码的主要功能是力信息采集及力信息滤波处理
1. 通过ROS中的rate函数控制机械臂力信息的采样频率和时间限制
2. 共有两个话题：force_seg和force，两个话题的的消息类型都是简单的Float64MultiArray为了简单，并未使用力传感器的标准消息类型。其中force是滤波前，force_seg是滤波后
3. 同时写入到了两个csv文件中
4. 采用python的signal包的信号滤波函数进行实时信号处理。
