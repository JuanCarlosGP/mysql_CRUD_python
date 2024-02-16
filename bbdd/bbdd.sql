CREATE DATABASE IF NOT EXISTS empleados;

USE empleados;

CREATE TABLE `mae_empleados` (
    `codigo` VARCHAR(4) NOT NULL,
    `nombre` VARCHAR(30) NOT NULL,
    `apellidos` VARCHAR(45) NOT NULL,
    `nif` VARCHAR(9) NOT NULL,
    `departamento` VARCHAR(15) NOT NULL,
    `num_hijos` INT NOT NULL,
    PRIMARY KEY(`codigo`)
    );
DROP TABLE mae_empleados;