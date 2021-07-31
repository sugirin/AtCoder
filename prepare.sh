contest=$1

mkdir -p src/${contest}
for q in a b c d e f g h; do
cat - <<EOF >src/${contest}/${contest}_${q}.py
"""
https://atcoder.jp/contests/${contest}/tasks/${contest}_${q}
"""
EOF
done
