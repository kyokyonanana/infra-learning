# ---- ステージ1: ビルド ----
FROM golang:1.23-alpine AS build
WORKDIR /src
COPY go.mod ./
COPY main.go ./
RUN CGO_ENABLED=0 go build -o /app .

# ---- ステージ2: 実行 ----
FROM scratch
COPY --from=build /app /app
USER 65534:65534
EXPOSE 8080
ENTRYPOINT ["/app"]
