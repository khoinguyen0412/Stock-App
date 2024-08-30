FROM php:8.2-rc-fpm

ADD . .

RUN apt-get update && apt-get install -y \
    git \
    curl \
    libpng-dev \
    libonig-dev \
    libxml2-dev \
    zip \
    unzip\
    libcurl4-openssl-dev\
    libbz2-dev 


# Clear cache
RUN apt-get clean && rm -rf /var/lib/apt/lists/*


# Install PHP extensions
RUN docker-php-ext-install bz2 bcmath calendar date dom fileinfo filter gd hash iconv json libxml mbstring mysqlnd openssl pcre pdo_mysql random readline session standard tokenizer xml xmlreader xmlwriter zip zlib


COPY --from=composer:latest /usr/bin/composer /usr/bin/composer


CMD php artisan serve --host=0.0.0.0 --port=$APP_PORT