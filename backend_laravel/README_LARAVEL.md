# Laravel Backend - MCH Follow-Up System

This is the Laravel-based implementation of the Maternal and Child Health Follow-Up System.

## Requirements
- PHP >= 8.1
- Composer
- MySQL (XAMPP recommended)

## Setup Instructions
1. **Database**: Create a database named `mch_followup` in XAMPP MySQL.
2. **Installation**:
   ```bash
   cd backend_laravel
   composer install
   cp .env.example .env
   php artisan key:generate
   ```
3. **Configure .env**:
   Update the DB settings to match your XAMPP setup:
   ```env
   DB_CONNECTION=mysql
   DB_HOST=127.0.0.1
   DB_PORT=3306
   DB_DATABASE=mch_followup
   DB_USERNAME=root
   DB_PASSWORD=
   ```
4. **Migrations**:
   ```bash
   php artisan migrate
   ```
5. **Run Server**:
   ```bash
   php artisan serve
   ```

## Key Files
- **Models**: `app/Models/`
- **Controllers**: `app/Http/Controllers/API/`
- **Routes**: `routes/api.php`
- **Migrations**: `database/migrations/`
