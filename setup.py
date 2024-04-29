from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    """
    Returns the list of requirements

    Args:
        file_path (str): The path of the requirements.txt file
    

    Returns:
        List[str]: _description_
    """
    requirements = []
    
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        
        if '-e .' in requirements:
            requirements.remove('-e .')
            
    return requirements

setup(
    name = 'Student Performance Analysis',
    version = '0.0.1',
    author = 'Mercy Mukundi',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)