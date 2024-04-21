from promptflow import tool


@tool
def process_search_result(search_result):

    try:
        context = []
        for vis_info in search_result:
            context.append({
                "SID": vis_info[0],
                "RG": vis_info[1],
                "region": vis_info[2],
                "environment": vis_info[3],
                "App-VM-SKU": vis_info[4],
                "App-OS": vis_info[5],
                "App-OS-SKU": vis_info[6],
                "App-VM-count": vis_info[7],
                "App-VM-list": vis_info[8],
                "DB-VM-SKU": vis_info[9],
                "DB-OS": vis_info[10],
                "DB-OS-SKU": vis_info[11],
                "DB-VM-count": vis_info[12],
                "status": vis_info[13],
                "health": vis_info[14]
            })
        return context

    except Exception as e:
        print(f"Error: {e}")
        return ""
