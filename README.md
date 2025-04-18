# 🎬 MovieNest - Vue + Node + PostgreSQL

¡Bienvenido a **MovieNest**!  
Este proyecto es una aplicación completa para gestión de películas favoritas, listas personales y mucho más.

## 🚀 Requisitos Previos

- Docker y Docker Compose
- PostgreSQL

---

## ⚙️ Configuración Inicial

Antes de levantar el proyecto, es necesario realizar algunos ajustes en la configuración del entorno y base de datos:

### 📄 1. Variables de Entorno

Editá el archivo `.env` y el docker-compose de este contenedor con los siguientes datos:

```env
# 🎬 MovieNest - Vue + Node + PostgreSQL

¡Bienvenido a **MovieNest**!  
Este proyecto es una aplicación completa para gestión de películas favoritas, listas personales y mucho más.

## 🚀 Requisitos Previos

- Node.js >= 16
- Docker y Docker Compose
- PostgreSQL

---

## ⚙️ Configuración Inicial

Antes de levantar el proyecto, es necesario realizar algunos ajustes en la configuración del entorno y base de datos:

### 📄 1. Variables de Entorno

Editá el archivo `.env` (crealo si no existe) en la raíz del backend con los siguientes datos:

```env
- POSTGRES_DB=MovieNest
- POSTGRES_USER=tu usuario #cambiar el usuario
- POSTGRES_PASSWORD=tu contraseña #cambiar la contraseña
- POSTGRES_HOST=host.docker.internal
- POSTGRES_PORT=5433

