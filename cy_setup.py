from Cython.Build import cythonize, build_ext
from setuptools import setup
from setuptools.extension import Extension
from pathlib import Path
import shutil

py_files = [
]


def GenExtensions():
    return [Extension(name=f.split('.py')[0], sources=[f]) for f in py_files] + [Extension(name='*', sources=['tx_run.py'])]


class MyBuildExt(build_ext):
    def run(self):
        build_ext.run(self)

        build_dir = Path(self.build_lib)
        root_dir = Path(__file__).parent

        target_dir = build_dir if not self.inplace else root_dir

        for p in Path('.').glob('*.py'):
            if str(p) not in ["cy_setup.py"]+py_files:
                self.copy_file(p, root_dir, target_dir)
        for p in Path('.').glob('*.service'):
            self.copy_file(p, root_dir, target_dir)
        self.copy_dir('rgw/http_handlers', root_dir, target_dir)
        self.copy_dir('rgwv2', root_dir, target_dir)
        self.copy_dir('static', root_dir, target_dir)
        self.copy_dir('staticfiles', root_dir, target_dir)

    def ignore_callback(self, src, names):
        import re
        pattern = re.compile(r"[\w.-]+\.pyc")
        ignored_names = set()
        for name in names:
            if pattern.match(name):
                ignored_names.add(name)
        return ignored_names

    def copy_dir(self, path, source_dir, destination_dir):
        if not (source_dir / path).exists():
            return
        shutil.copytree(str(source_dir / path), str(destination_dir / path), ignore=self.ignore_callback)

    def copy_file(self, path, source_dir, destination_dir):
        if not (source_dir / path).exists():
            return
        shutil.copyfile(str(source_dir / path), str(destination_dir / path))

setup(
    ext_modules=cythonize(GenExtensions(),
                          compiler_directives={'language_level': 3,
                                               'always_allow_keywords': True}),
    cmdclass=dict(build_ext=MyBuildExt)
)

