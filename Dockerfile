# Use the Nginx image from Docker Hub
FROM nginx:alpine

# Remove default Nginx index page
RUN rm -rf /usr/share/nginx/html/*

# Copy custom HTML files to the container
COPY welcome.html /usr/share/nginx/html/welcome.html
COPY thankyou.html /usr/share/nginx/html/thankyou.html

# Create a symbolic link to set welcome.html as the default index page
RUN ln -s /usr/share/nginx/html/welcome.html /usr/share/nginx/html/index.html

# Expose port 80
EXPOSE 80

# Start Nginx and keep it running in the foreground
CMD ["nginx", "-g", "daemon off;"]
