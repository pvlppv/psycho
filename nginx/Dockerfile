FROM nginx:stable-alpine3.17-slim
EXPOSE 3000
RUN mkdir /app
COPY default.conf /etc/nginx/conf.d/default.conf
#COPY --from=build-stage /app/dist /app