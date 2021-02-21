echo "begin to build bookmark..."

mkdir -p bookmark

dirs=(cmd config const error logger task_factory)
for dir in ${dirs[*]}; do
    cp -r "${dir}" bookmark/
done

files=(bookmark.py bookmark.sh install.py uninstall.py util.py)
for file in ${files[*]}; do
    cp -r "${file}" bookmark/
done

tar zcvf bookmark.tar.gz bookmark/
rm -rf bookmark/
