function delete_chahe {
    base_dir=$(cd $(dirname "$0") && pwd)
    dir_list=$(find "${base_dir}" -name "__pycache__")
    for dir in ${dir_list[*]}; do
        rm -rf "${dir}"
    done
}


function build {
    package_name=$1
    mkdir -p bookmark

    dirs=(cmd config const error logger task_factory)
    for dir in ${dirs[*]}; do
        cp -r "${dir}" bookmark/
    done

    files=(bookmark.py install.py uninstall.py util.py)
    for file in ${files[*]}; do
        cp -r "${file}" bookmark/
    done

    tar zcvf "${package_name}" bookmark/
    rm -rf bookmark/
}

echo "begin to build bookmark..."

target_path=$1
package_name=bookmark.tar.gz
delete_chahe
build "${package_name}"
if [ -n "${target_path}" ]
then
    mv "${package_name}" "${target_path}"
fi

echo "build bookmark finished."
