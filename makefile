build:
	docker build -t sluan500/mcp-luan:latest .

push:
	docker push sluan500/mcp-luan:latest

run:
	docker run -p 8000:8000 sluan500/mcp-luan:latest