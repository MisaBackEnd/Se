build-grid:
	cd GridStandAlone && docker build -t "gridstandalone" .

start-grid:
	docker run --name GridStandAlone -v $(pwd)/GridStandAlone:/opt/app -p 4444:4444 -td gridstandalone