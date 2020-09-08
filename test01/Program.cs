using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Data.Entity;

namespace test
{
    class Program
    {
        static void Main(string[] args)
        {
            var db = new northwndEntities();

            var products = from p in db.Products
                           select p;

            Console.WriteLine("產品資訊如下:");

            foreach (var p in products)
            {
                Console.WriteLine($"{p.ProductID}, {p.ProductName}, {p.UnitPrice}, {p.UnitsInStock}");
            }

            Console.WriteLine("請按任一鍵後離開...");
            Console.ReadKey();

            db.Dispose();   //關閉EF資料庫連線

        }
    }
}
