from ipykernel.kernelapp import IPKernelApp
from .kernel import CpsamdKernel

IPKernelApp.launch_instance(kernel_class=CpsamdKernel)
