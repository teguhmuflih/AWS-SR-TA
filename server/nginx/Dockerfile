# mengambil nginx image dari Docker Hub
FROM nginx

# menghapus konfigurasi default dari nginx dan menggantinya dengan yang baru
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d/