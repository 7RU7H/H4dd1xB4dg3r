use std::process::Command;
use console::style;
use log::{info, warn};
use std::{thread, time::Duration};
use anyhow::Result;
use crossbeam_channel::{bounded, tick, Receiver, select}; 

extern crate clap
use clap::{Arg, App};


#[derive(Parser, Debug)]
#[clap(author, version, about, long_about = None)]
struct Args {
    // Project path
    #[clap(parse(from_os_str))]
    project_path: std::path::PathBuf,
    // Target address, with or without CIDR notation or domain name
    #[clap(short, long, default_value_t = "127.0.0.1")]
    target: String,
}

async fn heartbeat() -> Result<String> {
    let ctrl_c_events = ctrl_channel()?;
    let ticks = tick(Duration::from_secs(1));

    loop {
        select! {
            recv(ticks) -> _ => {
                println!("working!");
            }
            recv(ctrl_c_events) -> _ => {
                println!();
                println!("Goodbye!");
                break;
            }
        }
    }

    Ok(())
}

fn create_progress_bar(quiet_mode: bool, msg: &str, length: Option<u64>) -> ProgressBar {
    let bar = match quiet_mode {
        true => ProgressBar::hidden(),
        false => {
            match length {
                Some(len) => ProgressBar::new(len),
                None => ProgressBar::new_spinner(),
            }
        }
    };

    bar.set_message(msg);
    match length.is_some() {
        true => bar
            .set_style(ProgressStyle::default_bar()
                .template("{msg} {spinner:.green} [{elapsed_precise}] [{wide_bar:.cyan/blue}] {bytes}/{total_bytes} eta: {eta}")
                .progress_chars("=> ")),
        false => bar.set_style(ProgressStyle::default_spinner()),
    };

    bar
}

fn ctrl_channel() -> Result<Receiver<()>, ctrlc::Error> {
    let (sender, receiver) = bounded(100);
    ctrlc::set_handler(move || {
        let _ = sender.send(());
    })?;

    Ok(receiver)
}

async fn progress_bar() -> Result<String> {
//https://github.com/console-rs/indicatif/blob/HEAD/examples/multi.rs
//want multi.rs
    let pb = indicatif::ProgressBar::new(100);
    for i in 0..100 {
        do_hard_work();
        pb.println(format!("[+] Finished #{}", i));
        pb.inc(1);
    }
    pb.finish_with_message("Done");
}

fn run_tool(tool_name: &str, tool_args: &str) { 
let tool_output = Command::new(tool_name)
        .arg(tool_args)
        .output()
        .expect("Failed to execute %s" tool_name);

return 
}

fn main() -> Result<()> {
    //cli stuff
    let args = Args::parse();
    let = App::new("")
        .version("0.1.0")
        .author("7ru7h")
        .about("Automated Recon")
        .arg(Arg::with_name("PROJECT_PATH")
                 .required(true)
                 .takes_value(true)
                 .index(1)
                 .help("Provide path ending with your proposed name of the project"))
        .get_matches();
        .arg(Arg::with_name("TARGET")
                 .required(true)
                 .takes_value(true)
                 .index(2)
                 .help("IP address, range or domain name"))
        .get_matches();
    let project_path = matches.value_of("PROJECT_PATH").unwrap();
    let target = matches.value_of("TARGET").unwrap();
    Ok(())
    println!("The output will be found at {} for the target: {}", project, target);

    env_logger::init();
    //logging
    info!("starting up");
    warn!("oops, nothing implemented!");
    
    target_initial_tests()
    output_directory_creation()
    
    heartbeat().await;
    progress_bar().await;

    let init_test = connection_test();
    block_on(init_test);
    let port_scan = port_scanning();
        //output
    collect_service_data();
    run_secondary_nmap().await;

    service_analysis();
    if webservice_found {
        construct_url()
        recon_webservices()
        if cms_found {
            //target.cms_identified -> tool_name
            //cms related scan
            }
        }
        recon_vhost() //consider await !!
    }
    if smbservice_found {
        smb_analysis()
    }


}

async fn recon_vhost() -> Result<TYPE> {
    let gobuster_vhost = run_tool()
}

async fn recon_webservices() -> Result<TYPE> {
    let vuln_analysis = web_analysis().await;
    let gospider_crawl = run_tool().await;  
    let feroxbuster_cd = web_content_discovery_feroxbuster().await;
    futures::join!(vuln_analysis, gospider_crawl, feroxbuster_cd);
}

async fn web_analysis() -> Result<TYPE> {
    let nikto_x = run_tool().await;
    let nuclei_scan = runt_tool().await;
}

async fn web_content_discovery_feroxbuster() -> Result<TYPE> {
    let feroxbuster_big = run_tool().await;
    let feroxbuster_common = run_tool().await;
    let feroxbuster_directory_medium = run_tool().await;
    futures::join!(feroxbuster_big, feroxbuster_common, feroxbuster_directory_medium);
    let url_listing = sort_found_urls();
}

    //web related - managed parallelism based on tool
        //gospider
        //nikto, nuclie
        //cms scan
        //feroxbuster
            //nmap scripting
    
    //smb related
            //nmap scripting
    //
    //strings formating target_ip variable into commands
//target_url


//listing of commands

//struct to store extracted data

//methods?
    
async fn connection_test() -> Result<TYPE> {
    let ping_output = run_tool().await;
    let nmap_sn_pn = run_tool().await;
    let traceroute = run_tool().await;
}

async fn port_scanning() -> Result<TYPE> {
    //masscan naabu_output = run_tool().await();
    initial_nmap = run_initial_nmap().await();
    futures::join!(//naabu_output, initial_nmap);
}

async fn run_initial_nmap() -> Result<TYPE> {
    //-sS and -Pn flag additions
    let nmap_extensive_output = run_tool().await;
}

async fn run_udp_nmap() -> Result<TYPE> {
    //-sS and -Pn flag additions
    //SPEED on this will take a while!
    let nmap_udp_output = run_tool().await;
}

async fn run_secondary_nmap() -> Result<TYPE> {
    //-sS and -Pn flag additions
    let nmap_discovery_output = run_tool().await;
    let nmap_vuln_output = run_tool().await;
    futures::join!(nmap_discovery_output, nmap_vuln_output;
}

async fn collect_service_data() -> Result<TYPE> {
    let all_ports = collect_portlist().await();
    let service_list = collect_services.await();
    futures::join!(all_ports, service_list);
}


async fn service_analysis_cntl

