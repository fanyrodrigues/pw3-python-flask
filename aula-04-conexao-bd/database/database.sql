-- --------------------------------------------------------
-- Servidor:                     127.0.0.1
-- Versão do servidor:           10.1.33-MariaDB - mariadb.org binary distribution
-- OS do Servidor:               Win32
-- HeidiSQL Versão:              9.5.0.5196
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Copiando estrutura do banco de dados para games
CREATE DATABASE IF NOT EXISTS `games` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `games`;

-- Copiando estrutura para tabela games.game
CREATE TABLE IF NOT EXISTS `game` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `titulo` varchar(150) DEFAULT NULL,
  `ano` int(11) DEFAULT NULL,
  `categoria` varchar(150) DEFAULT NULL,
  `plataforma` varchar(150) DEFAULT NULL,
  `preco` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

-- Copiando dados para a tabela games.game: ~3 rows (aproximadamente)
/*!40000 ALTER TABLE `game` DISABLE KEYS */;
INSERT INTO `game` (`id`, `titulo`, `ano`, `categoria`, `plataforma`, `preco`) VALUES
	(1, 'The Legend of Zelda: Breath of the Wild', 2017, 'Mundo Aberto', 'Nintendo Switch', 350),
	(2, 'Valorant', 2020, 'FPS', 'Multiplataforma', 0),
	(3, 'Minecraft', 2010, 'Sandbox', 'Multiplataforma', 120);
/*!40000 ALTER TABLE `game` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
