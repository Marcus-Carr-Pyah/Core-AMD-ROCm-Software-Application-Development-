import torch
print(f"PyTorch version: {torch.__version__}")
print(f"HIP available:   {torch.cuda.is_available()}")
print(f"HIP version:     {torch.version.hip}")
print(f"GPU:             {torch.cuda.get_device_name(0)}")
print(f"GPU memory:      {torch.cuda.get_device_properties(0).total_memory / (2**30):.1f} GB")