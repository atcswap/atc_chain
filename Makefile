build: 
	docker build -t atc_chain:latest .

deploy:	
	docker run -d --name atc_chain_1 atc_chain:latest sh -c "tail -f /dev/null"

test: 
	docker exec -it atc_chain_1 pytest tests