import png
import sys, json

def main(args):
    filepath = args[0]
    reader = png.Reader(filename=filepath)
    chunks = reader.chunks()
    chunk_list = list(chunks)
    
    prompt_chunk = chunk_list[1]
    prompt_data = prompt_chunk[1]
    # remove keyword and null character
    params_bytes = prompt_data[7:]
    
    prompt_dict = json.loads(params_bytes.decode('utf-8'))
    positive = prompt_dict['6']['inputs']['text']
    negative = prompt_dict['7']['inputs']['text']
    
    print("Positive:\n" + positive)
    print("Negative:\n" + negative)

if __name__ == "__main__":
    args = sys.argv[1:]
    main(args)