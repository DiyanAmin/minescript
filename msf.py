import m
import sys

def display(msg):
    m.echo(f'\n\n\n\n{msg}\n\n\n\n')

def row_wise_give(items:dict,rows:int=3):
    if len(items)>9:
        m.echo('Error: More items than columns')
    val=0
    while val!=rows:
        for i in items:
            m.execute(f'give @s {i} {items[i]}')
        val+=1

def cide(entity_name:str):
    m.execute(f'kill @e[type={entity_name}]')

#Job Functions-----------------------------------

def read_jobs():
    '''
    Reads no. of jobs running from global_jobs.txt (Create if not created
    and enter default data as: "0,0," 
    and BOTH the commas are important 
    Place in the same folder as minescript folder NOT IN SAME FOLDER AS THIS FILE!!!!!!!)

    Returns
    -------

    data,
    A dictionary with length 2, keys being "jobs_running" and "highest_job_id" but you don't real need that because these funcs and job.py handle it for you :)
    '''
    data = {'jobs_running':0,'highest_job_id':0}
    content = ''
    with open('global_jobs.txt','r') as f:
        content = f.read()

    bit = ''
    val=1
    for i in content:
        if i==',':
            if val==1:
                data['jobs_running'] = int(bit)
                bit=''
                val=2
                continue
            elif val==2:
                data['highest_job_id'] = int(bit)
                bit=''
                break
        else:
            bit+=i
    return data

def write_jobs(jobs_data:dict):
    '''
    Similiar or opposite I guess to read_jobs(). Writes data to global_jobs.txt (again make if not made. Details in read_jobs()'s docstring)
    
    :param jobs_data: Should have length as 2. keys as (order DOES matter): "jobs_running" and "highest_job_id", respectively.
    :type jobs_data: dict
    '''
    new_content = f'{jobs_data['jobs_running']},{jobs_data['highest_job_id']},'
    with open('global_jobs.txt','w') as f:
        f.write(new_content)

def add_job(amt:int=1):
    '''
    Adds amt to total number of jobs.(default 1)
    
    :param amt: Amount of jobs to be added. CAN BE SET TO NEGATIVE INTEGERS (-1,-2,etc) FOR REDUCING JOBS
    :type amt: int
    '''
    current_jobs = read_jobs()
    write_jobs(
        {
            'jobs_running':((current_jobs['jobs_running'])+amt), #Add amt (default 1) to current jobs
            'highest_job_id':((current_jobs['highest_job_id'])+amt) #Add amt to highest job id
        }
    )
#------------------------------------------------

#Complex Data retrieving and storing functions------------

from diyanLib.data import json_handler #See https://github.com/DiyanAmin/diyanLib

def write_json(data:dict|str,dictionary:int=1):
    '''
    Writes complex data to a json file.
    
    :param data: The data. Can be dictionary or string.
    :type data: dict or str
    :param dictionary: Dictionary number (default 1).
    :type dictionary: int
    '''

    if dictionary!=-1:
        json_handler(f'jsons\\gd{dictionary}').save(data)
    elif dictionary==-1:
        json_handler('jsons\\minescript_data').save(data)
    else:
        m.echo('Invalid dictionary number')

def get_json(dict_num:str):
    '''
    Gets complex stored data.
    
    :param dict_num: Dictionary number
    :type dict_num: str

    :return: Dictionary of the data
    :rtype: dict
    '''
    if dict_num!=-1:
        datum = json_handler(f'jsons\\gd{dict_num}').get()
    elif dict_num==-1:
        datum = json_handler(f'jsons\\minescript_data').get()
    else:
        m.echo('Invalid dictionary number')
        datum='3RR0R'
    return datum

#--------------------------------------------------------------------------------------



#Block/Entity Scanner
def scan(filter:bool=False,filter_list:list=[],search:bool=False,search_list:list=[],type:str='blocks',radius:int=50):
    '''

    Scans for nearby blocks or entities
    
    :param filter: Enable filter or not. (Disabled by default) Filtered items are ignored in scan
    :type filter: bool
    :param filter_list: List or blocks/entities to filter out.
    :type filter_list: list
    :param search: Search for specific entities/blocks
    :type search: bool
    :param search_list: List of items to search for.
    :type search_list: list
    :param type: Scan type. blocks/entities
    :type type: str
    :param radius: Radius of scan. (Only applicable for blocks)
    :type radius: str
    '''

    x,y,z = get_pos()


    if type=='blocks':
        block_list = []
        radius_1 = [
            [x+1,y,z],
            [x,y,z-1],
            [x-1,y,z],
            [x,y,z+1]
        ]

        return radius_1,m.getblocklist([i for i in radius_1])

    
#ULILITY FUNCTION(S) (mainly for comfort)
def get_args():
    return len(sys.argv)-1 #Since we dont count file name

def get_pos():
    return int(m.player_position()[0]),int(m.player_position()[1])-1,int(m.player_position()[2])


#Init Funcs

write_json(
    {
        "username":m.player_name(),
        "bridging_cords":[-120,-22,178]
    },-1
)