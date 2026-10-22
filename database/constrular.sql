-- MySQL dump 10.13  Distrib 8.0.43, for Win64 (x86_64)
--
-- Host: localhost    Database: constrular
-- ------------------------------------------------------
-- Server version	8.0.43

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `categorias`
--

DROP TABLE IF EXISTS `categorias`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categorias` (
  `id_categoria` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) NOT NULL,
  PRIMARY KEY (`id_categoria`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categorias`
--

LOCK TABLES `categorias` WRITE;
/*!40000 ALTER TABLE `categorias` DISABLE KEYS */;
INSERT INTO `categorias` VALUES (1,'Materiais de Construção'),(2,'Ferramentas'),(3,'Elétrica'),(4,'Hidráulica'),(5,'Pintura');
/*!40000 ALTER TABLE `categorias` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `clientes`
--

DROP TABLE IF EXISTS `clientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clientes` (
  `id_cliente` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(150) NOT NULL,
  `cpf` varchar(14) DEFAULT NULL,
  `telefone` varchar(20) DEFAULT NULL,
  `email` varchar(150) DEFAULT NULL,
  `cidade` varchar(100) DEFAULT NULL,
  `estado` char(2) DEFAULT NULL,
  PRIMARY KEY (`id_cliente`),
  UNIQUE KEY `uk_clientes_cpf` (`cpf`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clientes`
--

LOCK TABLES `clientes` WRITE;
/*!40000 ALTER TABLE `clientes` DISABLE KEYS */;
INSERT INTO `clientes` VALUES (1,'João da Silva','123.456.789-01','(12) 98888-1001','joao@email.com','Guaratinguetá','SP'),(2,'Maria Oliveira','234.567.890-12','(12) 98888-1002','maria@email.com','Lorena','SP'),(3,'Carlos Santos','345.678.901-23','(12) 98888-1003','carlos@email.com','Taubaté','SP'),(4,'Ana Souza','456.789.012-34','(12) 98888-1004','ana@email.com','Pindamonhangaba','SP'),(5,'Pedro Costa','567.890.123-45','(12) 98888-1005','pedro@email.com','Guaratinguetá','SP');
/*!40000 ALTER TABLE `clientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fornecedores`
--

DROP TABLE IF EXISTS `fornecedores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fornecedores` (
  `id_fornecedor` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(150) NOT NULL,
  `telefone` varchar(20) DEFAULT NULL,
  `email` varchar(150) DEFAULT NULL,
  `cidade` varchar(100) DEFAULT NULL,
  `estado` char(2) DEFAULT NULL,
  PRIMARY KEY (`id_fornecedor`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fornecedores`
--

LOCK TABLES `fornecedores` WRITE;
/*!40000 ALTER TABLE `fornecedores` DISABLE KEYS */;
INSERT INTO `fornecedores` VALUES (1,'Construmais Distribuidora','(12) 99999-1001','contato@construmais.com','Guaratinguetá','SP'),(2,'Ferramentas Brasil','(12) 99999-1002','vendas@ferramentasbrasil.com','Lorena','SP'),(3,'Elétrica São Paulo','(12) 99999-1003','contato@eletricasp.com','São José dos Campos','SP'),(4,'Hidro Center','(12) 99999-1004','vendas@hidrocenter.com','Taubaté','SP'),(5,'Tintas Vale','(12) 99999-1005','contato@tintasvale.com','Pindamonhangaba','SP');
/*!40000 ALTER TABLE `fornecedores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `funcionarios`
--

DROP TABLE IF EXISTS `funcionarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `funcionarios` (
  `id_funcionario` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(150) NOT NULL,
  `cargo` varchar(100) DEFAULT NULL,
  `salario` decimal(10,2) DEFAULT NULL,
  `telefone` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id_funcionario`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `funcionarios`
--

LOCK TABLES `funcionarios` WRITE;
/*!40000 ALTER TABLE `funcionarios` DISABLE KEYS */;
INSERT INTO `funcionarios` VALUES (1,'Roberto Almeida','Gerente',4500.00,'(12) 97777-1001'),(2,'Juliana Martins','Vendedora',2800.00,'(12) 97777-1002'),(3,'Marcos Ferreira','Vendedor',2800.00,'(12) 97777-1003'),(4,'Fernanda Lima','Caixa',2500.00,'(12) 97777-1004'),(5,'Lucas Pereira','Estoquista',2400.00,'(12) 97777-1005');
/*!40000 ALTER TABLE `funcionarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `itens_venda`
--

DROP TABLE IF EXISTS `itens_venda`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `itens_venda` (
  `id_item` int NOT NULL AUTO_INCREMENT,
  `venda_id` int NOT NULL,
  `produto_id` int NOT NULL,
  `quantidade` int NOT NULL,
  `preco_unitario` decimal(10,2) NOT NULL,
  PRIMARY KEY (`id_item`),
  KEY `idx_itens_venda_venda` (`venda_id`),
  KEY `idx_itens_venda_produto` (`produto_id`),
  CONSTRAINT `fk_itens_venda_produtos` FOREIGN KEY (`produto_id`) REFERENCES `produtos` (`id_produto`),
  CONSTRAINT `fk_itens_venda_vendas` FOREIGN KEY (`venda_id`) REFERENCES `vendas` (`id_venda`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `itens_venda`
--

LOCK TABLES `itens_venda` WRITE;
/*!40000 ALTER TABLE `itens_venda` DISABLE KEYS */;
INSERT INTO `itens_venda` VALUES (1,1,1,2,38.00),(2,1,3,1,42.00),(3,2,4,1,279.90),(4,2,6,2,21.90),(5,3,7,3,29.90),(6,4,9,1,259.90),(7,4,10,2,32.90),(8,5,8,1,79.90),(9,5,2,2,27.00);
/*!40000 ALTER TABLE `itens_venda` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `movimentacoes_estoque`
--

DROP TABLE IF EXISTS `movimentacoes_estoque`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `movimentacoes_estoque` (
  `id_movimentacao` int NOT NULL AUTO_INCREMENT,
  `produto_id` int NOT NULL,
  `tipo` varchar(20) NOT NULL,
  `quantidade` int NOT NULL,
  `data_movimentacao` datetime NOT NULL,
  `observacao` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_movimentacao`),
  KEY `idx_movimentacoes_produto` (`produto_id`),
  CONSTRAINT `fk_movimentacoes_estoque_produtos` FOREIGN KEY (`produto_id`) REFERENCES `produtos` (`id_produto`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movimentacoes_estoque`
--

LOCK TABLES `movimentacoes_estoque` WRITE;
/*!40000 ALTER TABLE `movimentacoes_estoque` DISABLE KEYS */;
INSERT INTO `movimentacoes_estoque` VALUES (1,1,'ENTRADA',50,'2026-08-11 16:31:40','Compra inicial de estoque'),(2,2,'ENTRADA',30,'2026-08-11 16:31:40','Compra inicial de estoque'),(3,3,'ENTRADA',15,'2026-08-11 16:31:40','Compra inicial de estoque'),(4,4,'ENTRADA',8,'2026-08-11 16:31:40','Compra inicial de estoque'),(5,5,'ENTRADA',20,'2026-08-11 16:31:40','Compra inicial de estoque'),(6,6,'ENTRADA',40,'2026-08-11 16:31:40','Compra inicial de estoque'),(7,7,'ENTRADA',30,'2026-08-11 16:31:40','Compra inicial de estoque'),(8,8,'ENTRADA',15,'2026-08-11 16:31:40','Compra inicial de estoque'),(9,9,'ENTRADA',10,'2026-08-11 16:31:40','Compra inicial de estoque'),(10,10,'ENTRADA',20,'2026-08-11 16:31:40','Compra inicial de estoque'),(11,1,'SAIDA',5,'2026-08-11 16:31:40','Venda de 5 unidades');
/*!40000 ALTER TABLE `movimentacoes_estoque` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produtos`
--

DROP TABLE IF EXISTS `produtos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `produtos` (
  `id_produto` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(150) NOT NULL,
  `descricao` text,
  `preco_custo` decimal(10,2) NOT NULL,
  `preco_venda` decimal(10,2) NOT NULL,
  `estoque_minimo` int NOT NULL,
  `categoria_id` int NOT NULL,
  `fornecedor_id` int NOT NULL,
  PRIMARY KEY (`id_produto`),
  KEY `idx_produtos_categoria` (`categoria_id`),
  KEY `idx_produtos_fornecedor` (`fornecedor_id`),
  CONSTRAINT `fk_produtos_categorias` FOREIGN KEY (`categoria_id`) REFERENCES `categorias` (`id_categoria`),
  CONSTRAINT `fk_produtos_fornecedores` FOREIGN KEY (`fornecedor_id`) REFERENCES `fornecedores` (`id_fornecedor`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produtos`
--

LOCK TABLES `produtos` WRITE;
/*!40000 ALTER TABLE `produtos` DISABLE KEYS */;
INSERT INTO `produtos` VALUES (1,'Cimento CP-II 50kg','Cimento Portland CP-II saco de 50kg',28.00,38.00,20,1,1),(2,'Argamassa AC-II 20kg','Argamassa colante AC-II',18.00,27.00,15,1,1),(3,'Martelo de Unha','Martelo de aço com cabo de madeira',25.00,42.00,10,2,2),(4,'Furadeira de Impacto','Furadeira de impacto 650W',180.00,279.90,5,2,2),(5,'Fio Flexível 2,5mm','Rolo de fio elétrico flexível 2,5mm',95.00,139.90,10,3,3),(6,'Disjuntor 20A','Disjuntor monopolar 20A',12.00,21.90,20,3,3),(7,'Tubo PVC 25mm','Tubo PVC para instalação hidráulica',18.00,29.90,15,4,4),(8,'Torneira de Parede','Torneira metálica para parede',45.00,79.90,8,4,4),(9,'Tinta Acrílica 18L','Tinta acrílica para paredes internas e externas',180.00,259.90,5,5,5),(10,'Rolo de Pintura 23cm','Rolo de lã para pintura 23cm',18.00,32.90,10,5,5);
/*!40000 ALTER TABLE `produtos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vendas`
--

DROP TABLE IF EXISTS `vendas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vendas` (
  `id_venda` int NOT NULL AUTO_INCREMENT,
  `data_venda` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `cliente_id` int NOT NULL,
  `funcionario_id` int NOT NULL,
  `forma_pagamento` varchar(30) NOT NULL,
  PRIMARY KEY (`id_venda`),
  KEY `idx_vendas_cliente` (`cliente_id`),
  KEY `idx_vendas_funcionario` (`funcionario_id`),
  CONSTRAINT `fk_vendas_clientes` FOREIGN KEY (`cliente_id`) REFERENCES `clientes` (`id_cliente`),
  CONSTRAINT `fk_vendas_funcionarios` FOREIGN KEY (`funcionario_id`) REFERENCES `funcionarios` (`id_funcionario`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vendas`
--

LOCK TABLES `vendas` WRITE;
/*!40000 ALTER TABLE `vendas` DISABLE KEYS */;
INSERT INTO `vendas` VALUES (1,'2026-08-11 16:31:40',1,2,'PIX'),(2,'2026-08-11 16:31:40',2,3,'Cartao de Credito'),(3,'2026-08-11 16:31:40',3,2,'Dinheiro'),(4,'2026-08-11 16:31:40',4,4,'PIX'),(5,'2026-08-11 16:31:40',5,3,'Cartao de Debito');
/*!40000 ALTER TABLE `vendas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `vw_analise_financeira`
--

DROP TABLE IF EXISTS `vw_analise_financeira`;
/*!50001 DROP VIEW IF EXISTS `vw_analise_financeira`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `vw_analise_financeira` AS SELECT 
 1 AS `id_produto`,
 1 AS `produto`,
 1 AS `quantidade_vendida`,
 1 AS `faturamento`,
 1 AS `custo_total`,
 1 AS `lucro`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `vw_estoque`
--

DROP TABLE IF EXISTS `vw_estoque`;
/*!50001 DROP VIEW IF EXISTS `vw_estoque`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `vw_estoque` AS SELECT 
 1 AS `id_produto`,
 1 AS `produto`,
 1 AS `categoria`,
 1 AS `fornecedor`,
 1 AS `preco_custo`,
 1 AS `preco_venda`,
 1 AS `estoque_minimo`,
 1 AS `estoque_atual`,
 1 AS `status_estoque`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `vw_faturamento_funcionarios`
--

DROP TABLE IF EXISTS `vw_faturamento_funcionarios`;
/*!50001 DROP VIEW IF EXISTS `vw_faturamento_funcionarios`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `vw_faturamento_funcionarios` AS SELECT 
 1 AS `id_funcionario`,
 1 AS `funcionario`,
 1 AS `quantidade_vendas`,
 1 AS `total_vendido`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `vw_faturamento_pagamento`
--

DROP TABLE IF EXISTS `vw_faturamento_pagamento`;
/*!50001 DROP VIEW IF EXISTS `vw_faturamento_pagamento`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `vw_faturamento_pagamento` AS SELECT 
 1 AS `forma_pagamento`,
 1 AS `quantidade_vendas`,
 1 AS `faturamento`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `vw_produtos_mais_vendidos`
--

DROP TABLE IF EXISTS `vw_produtos_mais_vendidos`;
/*!50001 DROP VIEW IF EXISTS `vw_produtos_mais_vendidos`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `vw_produtos_mais_vendidos` AS SELECT 
 1 AS `id_produto`,
 1 AS `produto`,
 1 AS `quantidade_vendida`,
 1 AS `faturamento`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `vw_vendas`
--

DROP TABLE IF EXISTS `vw_vendas`;
/*!50001 DROP VIEW IF EXISTS `vw_vendas`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `vw_vendas` AS SELECT 
 1 AS `id_venda`,
 1 AS `data_venda`,
 1 AS `cliente`,
 1 AS `funcionario`,
 1 AS `produto`,
 1 AS `quantidade`,
 1 AS `preco_unitario`,
 1 AS `subtotal`,
 1 AS `forma_pagamento`*/;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `vw_analise_financeira`
--

/*!50001 DROP VIEW IF EXISTS `vw_analise_financeira`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `vw_analise_financeira` AS select `p`.`id_produto` AS `id_produto`,`p`.`nome` AS `produto`,sum(`iv`.`quantidade`) AS `quantidade_vendida`,sum((`iv`.`quantidade` * `iv`.`preco_unitario`)) AS `faturamento`,sum((`iv`.`quantidade` * `p`.`preco_custo`)) AS `custo_total`,(sum((`iv`.`quantidade` * `iv`.`preco_unitario`)) - sum((`iv`.`quantidade` * `p`.`preco_custo`))) AS `lucro` from (`itens_venda` `iv` join `produtos` `p` on((`iv`.`produto_id` = `p`.`id_produto`))) group by `p`.`id_produto`,`p`.`nome` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `vw_estoque`
--

/*!50001 DROP VIEW IF EXISTS `vw_estoque`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `vw_estoque` AS select `p`.`id_produto` AS `id_produto`,`p`.`nome` AS `produto`,`c`.`nome` AS `categoria`,`f`.`nome` AS `fornecedor`,`p`.`preco_custo` AS `preco_custo`,`p`.`preco_venda` AS `preco_venda`,`p`.`estoque_minimo` AS `estoque_minimo`,coalesce(sum((case when (`me`.`tipo` = 'ENTRADA') then `me`.`quantidade` when (`me`.`tipo` = 'SAIDA') then -(`me`.`quantidade`) else 0 end)),0) AS `estoque_atual`,(case when (coalesce(sum((case when (`me`.`tipo` = 'ENTRADA') then `me`.`quantidade` when (`me`.`tipo` = 'SAIDA') then -(`me`.`quantidade`) else 0 end)),0) <= 0) then 'CRITICO' when (coalesce(sum((case when (`me`.`tipo` = 'ENTRADA') then `me`.`quantidade` when (`me`.`tipo` = 'SAIDA') then -(`me`.`quantidade`) else 0 end)),0) < `p`.`estoque_minimo`) then 'ATENCAO' else 'NORMAL' end) AS `status_estoque` from (((`produtos` `p` join `categorias` `c` on((`p`.`categoria_id` = `c`.`id_categoria`))) join `fornecedores` `f` on((`p`.`fornecedor_id` = `f`.`id_fornecedor`))) left join `movimentacoes_estoque` `me` on((`p`.`id_produto` = `me`.`produto_id`))) group by `p`.`id_produto`,`p`.`nome`,`c`.`nome`,`f`.`nome`,`p`.`preco_custo`,`p`.`preco_venda`,`p`.`estoque_minimo` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `vw_faturamento_funcionarios`
--

/*!50001 DROP VIEW IF EXISTS `vw_faturamento_funcionarios`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `vw_faturamento_funcionarios` AS select `f`.`id_funcionario` AS `id_funcionario`,`f`.`nome` AS `funcionario`,count(distinct `v`.`id_venda`) AS `quantidade_vendas`,sum((`iv`.`quantidade` * `iv`.`preco_unitario`)) AS `total_vendido` from ((`funcionarios` `f` join `vendas` `v` on((`f`.`id_funcionario` = `v`.`funcionario_id`))) join `itens_venda` `iv` on((`v`.`id_venda` = `iv`.`venda_id`))) group by `f`.`id_funcionario`,`f`.`nome` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `vw_faturamento_pagamento`
--

/*!50001 DROP VIEW IF EXISTS `vw_faturamento_pagamento`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `vw_faturamento_pagamento` AS select `v`.`forma_pagamento` AS `forma_pagamento`,count(distinct `v`.`id_venda`) AS `quantidade_vendas`,sum((`iv`.`quantidade` * `iv`.`preco_unitario`)) AS `faturamento` from (`vendas` `v` join `itens_venda` `iv` on((`v`.`id_venda` = `iv`.`venda_id`))) group by `v`.`forma_pagamento` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `vw_produtos_mais_vendidos`
--

/*!50001 DROP VIEW IF EXISTS `vw_produtos_mais_vendidos`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `vw_produtos_mais_vendidos` AS select `p`.`id_produto` AS `id_produto`,`p`.`nome` AS `produto`,sum(`iv`.`quantidade`) AS `quantidade_vendida`,sum((`iv`.`quantidade` * `iv`.`preco_unitario`)) AS `faturamento` from (`produtos` `p` join `itens_venda` `iv` on((`p`.`id_produto` = `iv`.`produto_id`))) group by `p`.`id_produto`,`p`.`nome` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `vw_vendas`
--

/*!50001 DROP VIEW IF EXISTS `vw_vendas`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `vw_vendas` AS select `v`.`id_venda` AS `id_venda`,`v`.`data_venda` AS `data_venda`,`c`.`nome` AS `cliente`,`f`.`nome` AS `funcionario`,`p`.`nome` AS `produto`,`iv`.`quantidade` AS `quantidade`,`iv`.`preco_unitario` AS `preco_unitario`,(`iv`.`quantidade` * `iv`.`preco_unitario`) AS `subtotal`,`v`.`forma_pagamento` AS `forma_pagamento` from ((((`vendas` `v` join `clientes` `c` on((`v`.`cliente_id` = `c`.`id_cliente`))) join `funcionarios` `f` on((`v`.`funcionario_id` = `f`.`id_funcionario`))) join `itens_venda` `iv` on((`v`.`id_venda` = `iv`.`venda_id`))) join `produtos` `p` on((`iv`.`produto_id` = `p`.`id_produto`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-08-11 16:33:07
