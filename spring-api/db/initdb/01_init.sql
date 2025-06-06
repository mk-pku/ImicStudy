USE mydb;

-- Category
CREATE TABLE IF NOT EXISTS `費目` (
	`id` INT AUTO_INCREMENT PRIMARY KEY,
	`name` VARCHAR(20) NOT NULL,
	`notes` VARCHAR(100) DEFAULT NULL,
	`created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	`updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Transaction
CREATE TABLE IF NOT EXISTS `家計簿` (
	`id` INT AUTO_INCREMENT PRIMARY KEY,
	`date` DATE NOT NULL,
	`category_id` INT NOT NULL,
	`memo` VARCHAR(100) DEFAULT NULL,
	`income` INT NOT NULL DEFAULT 0,
	`expenditure` INT NOT NULL DEFAULT 0,
	`created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	`updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	INDEX (`category_id`),
	CONSTRAINT `fk_category`
		FOREIGN KEY (`category_id`) REFERENCES `費目` (`id`)
		ON DELETE CASCADE
		ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Sample data
INSERT INTO `費目` (`name`, `notes`) VALUES 
	('食費', '毎日の食事代'),
	('光熱費', '電気・ガス・水道代');
INSERT INTO `家計簿` (`date`, `category_id`, `memo`, `income`, `expenditure`) VALUES
	('2025-06-01', 1, 'スーパーで買い物', 0, 5000),
	('2025-06-02', 2, '電気代支払い', 0, 8000);
