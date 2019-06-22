using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Threading;
using System.Web;
using System.Web.Mvc;

namespace WebApplication1.Controllers
{
    public class HomeController : Controller
    {
        public object Logger { get; private set; }

        public ActionResult Index()
        {
            return View();
        }

        [HttpPost]
        public ActionResult Index(HttpPostedFileBase file)
        {
            string[] arr = new string[1];
            //arr[0] = @"H:\Study\Semester 11\Internship\WebApplication1\WebApplication1\Content\new.py";
            //arr[0] = @"E:\new.py";
            //arr[0] = @"C:\Statement\DBBL\DBBL.py";
            arr[0] = @"E:\Statement_Summarization\Python\DBBL.py";
            //arr[0] = @"~/Content/new.py";

            try
            {
                // Create An instance of the Process class responsible for starting the newly process.
                System.Diagnostics.Process process1 = new System.Diagnostics.Process();
                // Set the filename name of the file you want to execute/open
                //process1.StartInfo.FileName = @"~/Content/python.exe";
                //process1.StartInfo.FileName = @"D:\WebApplication1\WebApplication1\Content\python.exe";
                process1.StartInfo.FileName = @"C:\Statement\DBBL\venv\Scripts\python.exe";
                //process1.StartInfo.FileName = @"E:\Statement_Summarization\Python\venv\Scripts\python.exepython.exe";
                //process1.StartInfo.FileName = @"C:\Users\sezan\AppData\Local\Programs\Python\Python37python.exe";
                process1.StartInfo.Arguments = string.Format("{0}", arr[0]);

                // Start the process without blocking the current thread
                process1.Start();
                // you may wait until finish that executable
                process1.WaitForExit();
                //or you can wait for a certain time interval 
                //Thread.Sleep(20000);//Assume within 20 seconds it will finish processing. 
                process1.Close();
            }
            catch (Exception ex)
            {
                TempData["Error"] = ex.Message.ToString();
            }

            return View();
        }


        public ActionResult About()
        {
            ViewBag.Message = "Your application description page.";

            return View();
        }

        public ActionResult Contact()
        {
            ViewBag.Message = "Your contact page.";

            return View();
        }
    }
}