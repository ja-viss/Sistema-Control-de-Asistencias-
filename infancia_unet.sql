-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 23-06-2023 a las 15:59:41
-- Versión del servidor: 10.1.38-MariaDB
-- Versión de PHP: 7.3.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `infancia_unet`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `admi_unet`
--

CREATE TABLE `admi_unet` (
  `id_admi` varchar(4) COLLATE utf16_spanish_ci NOT NULL COMMENT 'ID del personal administrativo',
  `ced_admi` int(9) NOT NULL COMMENT 'cedula del personal administrativo',
  `nom_admi` varchar(20) COLLATE utf16_spanish_ci NOT NULL COMMENT 'nombre del personal administrativo',
  `ape_admi` varchar(20) COLLATE utf16_spanish_ci NOT NULL COMMENT 'apellido del personal administrativo',
  `estatus_admi` varchar(8) COLLATE utf16_spanish_ci NOT NULL COMMENT 'estatus del personal admnistrativo',
  `tel_admi` varchar(11) COLLATE utf16_spanish_ci NOT NULL COMMENT 'telefono del personal administrativo'
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_spanish_ci COMMENT='Infromacion del personal administrativo';

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `asistencias_infantes`
--

CREATE TABLE `asistencias_infantes` (
  `id_asis` int(4) NOT NULL COMMENT 'id de las asistencia de los infantes',
  `fecha_asis` date NOT NULL COMMENT 'fecha de las asistencias',
  `n_masculinos` int(3) NOT NULL COMMENT 'numero de niños asistentes',
  `n_femeninas` int(3) NOT NULL COMMENT 'numero de niñas asistentes'
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_spanish_ci COMMENT='Asistencia de Infantes';

--
-- Volcado de datos para la tabla `asistencias_infantes`
--

INSERT INTO `asistencias_infantes` (`id_asis`, `fecha_asis`, `n_masculinos`, `n_femeninas`) VALUES
(1444, '2023-06-13', 12, 13),
(3456, '2023-06-20', 23, 34);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `asistencia_unet`
--

CREATE TABLE `asistencia_unet` (
  `id_asistencia` int(4) NOT NULL COMMENT 'Id de la asistencia',
  `id_personal` varchar(4) COLLATE utf16_spanish_ci NOT NULL COMMENT 'id del personal',
  `fecha_asis` date NOT NULL COMMENT 'fecha de la asistencia',
  `hora_entrada` time NOT NULL COMMENT 'hora de entrada',
  `hora_salida` time NOT NULL COMMENT 'hora de salida'
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_spanish_ci COMMENT='Informacion de las Asistencias del Personal';

--
-- Volcado de datos para la tabla `asistencia_unet`
--

INSERT INTO `asistencia_unet` (`id_asistencia`, `id_personal`, `fecha_asis`, `hora_entrada`, `hora_salida`) VALUES
(1345, '447O', '0000-00-00', '08:02:34', '08:08:46'),
(3344, '447O', '2023-06-21', '08:05:25', '08:08:46');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `direc_unet`
--

CREATE TABLE `direc_unet` (
  `id_direc` varchar(4) COLLATE utf16_spanish_ci NOT NULL COMMENT 'ID del personal directivo',
  `ced_direc` int(9) NOT NULL COMMENT 'cedula del personal directivo',
  `nom_direc` varchar(20) COLLATE utf16_spanish_ci NOT NULL COMMENT 'nombre del personal directivo',
  `ape_direc` varchar(20) COLLATE utf16_spanish_ci NOT NULL COMMENT 'apellido dle personal directivo',
  `estatus_direc` varchar(8) COLLATE utf16_spanish_ci NOT NULL COMMENT 'estatus del personal directivo',
  `tel_direc` varchar(11) COLLATE utf16_spanish_ci NOT NULL COMMENT 'telefono del personal directivo'
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_spanish_ci COMMENT='Infromacion del personal Directivo';

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `doce_unet`
--

CREATE TABLE `doce_unet` (
  `id_docente` varchar(4) COLLATE utf16_spanish_ci NOT NULL COMMENT 'id del personal docente',
  `ced_docente` int(9) NOT NULL COMMENT 'cedula del personal docente',
  `nom_docente` varchar(20) COLLATE utf16_spanish_ci NOT NULL COMMENT 'nombre del personal docente',
  `ape_docente` varchar(20) COLLATE utf16_spanish_ci NOT NULL COMMENT 'apellido del personal docente',
  `grup_docente` varchar(1) CHARACTER SET ucs2 COLLATE ucs2_spanish_ci NOT NULL COMMENT 'grupo del personal docente',
  `estatus_docente` varchar(8) COLLATE utf16_spanish_ci NOT NULL COMMENT 'estatus del personas docente',
  `telefono` varchar(11) COLLATE utf16_spanish_ci NOT NULL COMMENT 'telefono del personal docente'
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_spanish_ci COMMENT='Infomracion del personal docente';

--
-- Volcado de datos para la tabla `doce_unet`
--

INSERT INTO `doce_unet` (`id_docente`, `ced_docente`, `nom_docente`, `ape_docente`, `grup_docente`, `estatus_docente`, `telefono`) VALUES
('280P', 11499280, 'Nubia', 'Contreras', 'A', 'Activa', '04149724850');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `obre_unet`
--

CREATE TABLE `obre_unet` (
  `id_obre` varchar(4) COLLATE utf16_spanish_ci NOT NULL COMMENT 'ID del personal obrero',
  `ced_obre` int(9) NOT NULL COMMENT 'cedula del personal obrero',
  `nom_obre` varchar(20) COLLATE utf16_spanish_ci NOT NULL COMMENT 'nombre del personal obrero',
  `ape_obre` varchar(20) COLLATE utf16_spanish_ci NOT NULL COMMENT 'apellidom del personal obrero',
  `estatus_obre` varchar(20) COLLATE utf16_spanish_ci NOT NULL COMMENT 'estatus del personal obrero',
  `tel_obre` varchar(11) CHARACTER SET utf32 COLLATE utf32_spanish_ci NOT NULL COMMENT 'telefono del personal obrero'
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_spanish_ci COMMENT='informacion del personal obrero';

--
-- Volcado de datos para la tabla `obre_unet`
--

INSERT INTO `obre_unet` (`id_obre`, `ced_obre`, `nom_obre`, `ape_obre`, `estatus_obre`, `tel_obre`) VALUES
('589O', 30338589, 'Gerardo Jose ', 'Mogollon Gamboa', 'Activo', '04249724850');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `personal`
--

CREATE TABLE `personal` (
  `id_personal` varchar(4) COLLATE utf16_spanish_ci NOT NULL COMMENT 'ID del personal en la Instutucion',
  `tipo_personal` varchar(20) COLLATE utf16_spanish_ci NOT NULL COMMENT 'tipo del personal'
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_spanish_ci COMMENT='ALmacenamiento de los ID del personal';

--
-- Volcado de datos para la tabla `personal`
--

INSERT INTO `personal` (`id_personal`, `tipo_personal`) VALUES
('280P', 'Docente'),
('447O', 'Obrero'),
('589O', 'Obrero');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `admi_unet`
--
ALTER TABLE `admi_unet`
  ADD PRIMARY KEY (`id_admi`);

--
-- Indices de la tabla `asistencias_infantes`
--
ALTER TABLE `asistencias_infantes`
  ADD PRIMARY KEY (`id_asis`);

--
-- Indices de la tabla `asistencia_unet`
--
ALTER TABLE `asistencia_unet`
  ADD PRIMARY KEY (`id_asistencia`),
  ADD KEY `fk_id_per` (`id_personal`);

--
-- Indices de la tabla `direc_unet`
--
ALTER TABLE `direc_unet`
  ADD PRIMARY KEY (`id_direc`);

--
-- Indices de la tabla `doce_unet`
--
ALTER TABLE `doce_unet`
  ADD PRIMARY KEY (`id_docente`);

--
-- Indices de la tabla `obre_unet`
--
ALTER TABLE `obre_unet`
  ADD PRIMARY KEY (`id_obre`);

--
-- Indices de la tabla `personal`
--
ALTER TABLE `personal`
  ADD PRIMARY KEY (`id_personal`);

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `asistencia_unet`
--
ALTER TABLE `asistencia_unet`
  ADD CONSTRAINT `fk_id_per` FOREIGN KEY (`id_personal`) REFERENCES `personal` (`id_personal`) ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
