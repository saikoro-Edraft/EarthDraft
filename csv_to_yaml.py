import csv
import yaml

# CSVファイルを読み込む
with open("earth_draft_pool.csv", "r", encoding="utf-8") as csv_file:
    csv_content = csv_file.read()

# データの入れ物を作成
yaml_structure = {
    "pool": {
        "version": "7.34",
        "cards": {
            "normal": [],
            "rare": [],
            "initial_distribution": []
        }
    }
}

# CSVをパースして振り分け
reader = csv.reader(csv_content.strip().split('\n'))
header = next(reader) # ヘッダーをスキップ

# カテゴリのマッピング（CSVの表記 → YAMLのキー）
category_map = {
    "ノーマル": "normal",
    "レア": "rare",
    "初期配布": "initial_distribution"
}

# セクションのマッピング（英語化）
section_map = {
    "メイン": "main",
    "エクストラ": "extra"
}

for row in reader:
    rarity_jp, section_jp, count_str, card_name = row
    
    # データを整形
    card_data = {
        "name": card_name,
        "count": int(count_str),
        "section": section_map.get(section_jp, section_jp) # マッピングになければそのまま
    }
    
    # 対応するカテゴリのリストに追加
    target_key = category_map.get(rarity_jp)
    if target_key:
        yaml_structure["pool"]["cards"][target_key].append(card_data)

# YAMLとして出力（日本語が文字化けしないように設定）
output_yaml = yaml.dump(yaml_structure, allow_unicode=True, sort_keys=False)

# 結果を表示（またはファイルに保存）
print(output_yaml)

# ファイルに保存する場合
with open("earth_draft_pool.yaml", "w", encoding="utf-8") as f:
    f.write(output_yaml)