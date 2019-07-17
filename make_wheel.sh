
#------------------------------------------------------------------------------------------------------
# Builds the manylinux wheels python version of novas
# Development of the docker image used to build the manylinux wheels is at https://github.com/pypa/manylinux
# The docker image itself is downloaded from quay.io/pypa/manylinux1_x86_64 
# A demo of the manylinux build system is at https://github.com/pypa/python-manylinux-demo
#
# Here is how I run the docker image on my windows system.
# I share the umkehr development folder with the docker image.
#
# docker run  -v C:\Users\nickl\Documents\Work\software\novas:/novas -i -t 41c74197534c /bin/bash
# cd /novas
# ./make_wheel.sh
#
# The manylinux wheels are written to folder wheelhouse
#------------------------------------------------------------------------------------------------------

/opt/python/cp37-cp37m/bin/python setup.py bdist_wheel -d wheelhouse
rm -rf build/
rm -rf novas_py.egg-info/

/opt/python/cp36-cp36m/bin/python setup.py bdist_wheel -d wheelhouse
rm -rf build/
rm -rf novas_py.egg-info/

/opt/python/cp35-cp35m/bin/python setup.py bdist_wheel -d wheelhouse
rm -rf build/
rm -rf novas_py.egg-info/

cd wheelhouse
for whl in *-linux_*.whl
do
  echo "$whl"
  auditwheel repair "$whl" 
done

cd wheelhouse
for whl in *-manylinux*.whl
do
  echo "$whl"
  mv "$whl" "../$whl" 
done
cd ../

rm -f *-linux_*.whl
rm -rf wheelhouse
cd ../
 
