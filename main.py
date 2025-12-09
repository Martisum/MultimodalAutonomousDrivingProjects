# 最终项目整合的main，如果大家只是验证自己的工程，请只编辑自己的module下的main.py
# 下面的代码仅测试当前环境能否正常使用torch和CUDA
import torch

if __name__ == "__main__":
    print(f"PyTorch 版本: {torch.__version__}")
    if torch.cuda.is_available():
        print("CUDA 状态: 可用 (True)")