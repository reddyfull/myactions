# Use the Nginx image from Docker Hub
# look for security checks in the code below

FROM nginx:alpine

# Remove default Nginx index page
RUN rm -rf /usr/share/nginx/html/*

# Create a new index.html file
RUN echo '<html>' > /usr/share/nginx/html/index.html
RUN echo '<head><title>Welcome Page</title></head>' >> /usr/share/nginx/html/index.html
RUN echo '<body><h1 style="font-weight:bold;">Welcome to the Release Tag deployments</h1></body>' >> /usr/share/nginx/html/index.html
RUN echo '</html>' >> /usr/share/nginx/html/index.html

# Expose port 80
EXPOSE 80

# Start Nginx and keep it running in the foreground
CMD ["nginx", "-g", "daemon off;"]
