import m
import sys
import pyperclip as c

func = sys.argv[1] #Either set or read.
if func=='set': #basically check other argvs for well stuff ig
    running = sys.argv[2]
    highest = sys.argv[3]
    data={
        'jobs_running':running,
        'highest_job_id':highest
    }
    m.msf.write_jobs(data)
    if len(sys.argv)==4:
        m.echo(f'\n\nSet number of jobs running to {running} and highest job ID to {highest}')
        c.copy(r'\job read')
        m.echo('Copied Read Command\n\n\n\n')
elif func=='read':
    jobs_data = m.msf.read_jobs()
    running = jobs_data['jobs_running']
    highest = jobs_data['highest_job_id']
    if len(sys.argv)==2:
        m.echo(f'\n\nNumber of jobs running is: {running}\nHighest job ID is: {highest}\n\n\n\n')
elif func=='kill':
    jobs_data = m.msf.read_jobs()
    running = jobs_data['jobs_running']
    highest = jobs_data['highest_job_id']
    val = 1
    while val!=(highest+1):
        m.execute(r'\killjob '+str(val))
        m.echo(f'Killed job {val}')
        m.msf.add_job(-1)
        val+=1
    m.echo('Killed all jobs.')