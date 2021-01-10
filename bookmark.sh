current_dir=$(pwd)
base_dir=$(cd $(dirname $0) && pwd)

cd "${base_dir}"
python bookmark.py $@
cd "${current_dir}"