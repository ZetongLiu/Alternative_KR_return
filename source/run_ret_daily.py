import subprocess
import os
import sys

def main():
 
    base_path="D:\Document\EPFL_Coursework\MasterThesis"
    venv_python = os.path.join(base_path, '.venv', 'Scripts', 'python.exe')
    script_path = os.path.join(base_path, 'Code', 'Alternative_KR_return', 'source', 'ret_curve_estimation.py')
    cmd = [
        venv_python,
        script_path,
        f'--idx_ver={3}',
        f'--use_maturity_mask={True}',
        f'--flg_mp={False}',
        f'--num_t_each_trunk={1000}',
        f'--R={10}',
        f'--l_fixed={10.0}',
        f'--alpha_fixed={0.05}',
        f'--delta_fixed={0.0}',
        f'--dir_out_base={"./Code/Alternative_KR_return/KR_ret_models/"}'
    ]

    # Run the command
    subprocess.run(cmd)

if __name__ == "__main__":
    main()

