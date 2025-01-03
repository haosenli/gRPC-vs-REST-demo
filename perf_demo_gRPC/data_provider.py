import time

DATA_SIZE = 1000000

# Generate data only once
START_TIME = time.time()
ITEMS = [
    {
        "id": i,
        "name": f"Item {i}",
        "description": f"""
			{i} Lorem ipsum odor amet, consectetuer adipiscing elit. 
			Aenean viverra nam cursus sagittis integer. Quisque 
			taciti cubilia massa dignissim risus eu eros hac. 
			Neque suscipit dictum pulvinar nunc pellentesque. 
			Porttitor sem donec eu tempor arcu tempus. 
			Fermentum donec ac magnis phasellus ante himenaeos. 
			Dui aliquet orci amet morbi aptent nam dapibus phasellus. 
			Porta vestibulum luctus aptent finibus aliquet ornare tortor fames. 
			Lacus sed dictum himenaeos dapibus urna phasellus. 
			Parturient sollicitudin donec velit a arcu risus sem. 
			Velit ridiculus felis hendrerit pellentesque lobortis potenti. 
			Dignissim suscipit vehicula ligula enim viverra aenean auctor volutpat. 
			Ante scelerisque et litora pulvinar urna, malesuada mauris arcu. 
			Etiam eros ex, condimentum conubia habitasse nec tristique sociosqu.
        	""",
    }
    for i in range(DATA_SIZE)
]
END_TIME = time.time()
print(f"Data generation took {END_TIME - START_TIME} seconds for {DATA_SIZE} items")


def get_items(count: int) -> list[dict[str]]:
    if count > len(ITEMS):
        return ITEMS

    return ITEMS[:count]
