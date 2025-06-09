-- カテゴリ初期データ
INSERT IGNORE INTO `費目` (`id`, `name`, `notes`) VALUES
	(1, '給料', '給与等の定期収入'),
	(18, '趣味・娯楽', '映画やゲーム等');

-- トランザクション初期データ
INSERT IGNORE INTO `家計簿` (`id`, `date`, `category_id`, `memo`, `income`, `expenditure`) VALUES
	(1, '2025-06-01', 1, 'Base - 趣味・娯楽1', 0, 5000),
	(2, '2025-06-02', 18, 'Base - 給料1', 300000, 0);