using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace test2
{
    class Program
    {
        static void Main(string[] args)
        {
            AddDataBasic(); //以foreach(){ Add()方法}新增Entity資料
            //AddData();      //以List<T>.Foreach(x=>{ Add()方法})Entity資料
            //AddRangeData(); //以AddRange()方法新增Entity資料

            DisplayData();  //顯示資料
        }

        //以foreach(){ Add()方法}新增Entity資料
        static void AddDataBasic()
        {
            //建立List泛型集合, 將User Entity加入集合中
            List<User> users = new List<User>
            {
                new User { UserName="聖殿祭司", Email="dotnetcool@gmail.com" },
                new User { UserName="David", Email="david@gmail.com"},
                new User { UserName="Mary", Email="mary@gmail.com"}
            };

            List<Blog> blogs = new List<Blog>
            {
                new Blog { BlogName="DotNet開發聖殿", Url="http://www.dotnetblog.com.tw", UserUserId=1 },
                new Blog { BlogName="David's Blog", Url="http://www.davidblog.com", UserUserId=2},
                new Blog { BlogName="Mary's Blog", Url="http://www.maryblog.com", UserUserId=3}
            };

            List<Post> posts = new List<Post>
            {
                new Post { Title="I am 聖殿祭司.", Content="I love Mvc!", BlogBlogId=1 },
                new Post { Title="I am David.", Content="I love Entity Framework!", BlogBlogId=2 },
                new Post { Title="I am Mary", Content="I love Razor!", BlogBlogId=3 }
            };

            //初始DbContext資料庫環境物件
            BlogContext context = new BlogContext();

            //檢查資料是否存在, 若無則新增資料
            if (context.Users.Any())
            {
                Console.WriteLine("樣本資料己存在, 不新增資料");
                return;
            }

            //將資料加入到Users實體中
            foreach (var item in users)
            {
                context.Users.Add(item);
            }

            context.SaveChanges();  //呼叫SaveChanges()儲存異動
            Console.WriteLine("Users資料新增完成.");

            //將資料加入到Blogs實體中
            foreach (var item in blogs)
            {
                context.Blog.Add(item);
            }

            context.SaveChanges();
            Console.WriteLine("Blogs資料新增完成.");


            //將資料加入到Posts實體中
            foreach (var item in posts)
            {
                context.Post.Add(item);
            }

            context.SaveChanges();

            //也可以用苦力語法建立單一筆Entity資料
            Post post = new Post();
            post.Title = "I am 祭司.";
            post.Content = "I love sports!";
            post.BlogBlogId = 1;
            context.Post.Add(post);
            context.SaveChanges();

            //或者用聰明一點的物件初始化語法建立Entity
            var easyPost = new Post { Title = "I am 奚江華.", Content = "I love coding!", BlogBlogId = 1 };
            context.Post.Add(easyPost);
            context.SaveChanges();

            Console.WriteLine("Posts資料新增完成.");

            Console.WriteLine("AddDataBasic()執行完成, 請按任意鍵離開...");
            Console.ReadKey();

            context.Dispose();  //關閉資料庫所佔連線
        }

        //以List<T>.Foreach(x=>{ Add()方法})新增Entity資料
        static void AddData()
        {
            //建立List集合
            List<User> users = new List<User>
            {
                new User { UserName="Bob", Email="bob@gmail.com" },
                new User { UserName="Johnson", Email="johnson@gmail.com"},
                new User { UserName="Lucy", Email="lucy@gmail.com"}
            };

            List<Blog> blogs = new List<Blog>
            {
                new Blog { BlogName="Bob's Blog", Url="http://www.bobblog.com.tw", UserUserId=4 },
                new Blog { BlogName="Johnson's Blog", Url="http://www.johnsonblog.com", UserUserId=5},
                new Blog { BlogName="Lucy's Blog", Url="http://www.lucyblog.com", UserUserId=6}
            };

            List<Post> posts = new List<Post>
            {
                new Post { Title="I am Tony.", Content="I love JavaScript!", BlogBlogId=4 },
                new Post { Title="I am David.", Content="I love jQuery Mobile!", BlogBlogId=5 },
                new Post { Title="I am Mary", Content="I love LINQ!", BlogBlogId=6 }
            };

            //將List加入到Entity集合
            BlogContext ctx = new BlogContext();

            ///檢查UserId為4的資料是否存在?若無則新增資料
            if (ctx.Users.Find(4) != null)
            {
                Console.WriteLine("樣本資料己存在, 不新增資料");
                return;
            }

            users.ForEach(x => ctx.Users.Add(x));
            ctx.SaveChanges();   //呼叫SaveChanges()儲存異動
            Console.WriteLine("Users資料新增完成.");

            blogs.ForEach(x => ctx.Blog.Add(x));
            ctx.SaveChanges();
            Console.WriteLine("Blogs資料新增完成.");

            posts.ForEach(x => ctx.Post.Add(x));
            ctx.SaveChanges();
            Console.WriteLine("Posts資料新增完成.");

            ctx.Dispose();

            Console.WriteLine("AddData()執行完成,請按任意鍵離開...");
            Console.ReadKey();
        }

        //以AddRange()方法新增Entity資料
        static void AddRangeData()
        {
            //建立List集合
            List<User> users = new List<User>
            {
                new User { UserName="John", Email="john@gmail.com" },
                new User { UserName="Tom", Email="tom@gmail.com"},
                new User { UserName="Rose", Email="rose@gmail.com"}
            };

            List<Blog> blogs = new List<Blog>
            {
                new Blog { BlogName="John's Blog", Url="http://www.johnblog.com", UserUserId=7 },
                new Blog { BlogName="Tom's Blog",  Url="http://www.tomblog.com", UserUserId=8 },
                new Blog { BlogName="Rose's Blog", Url="http://www.roseblog.com", UserUserId=9 },
                new Blog { BlogName="Code Magic碼魔法", Url="http://www.codemagic.com.tw", UserUserId=1 }

            };

            List<Post> posts = new List<Post>
            {
                new Post { Title="I am John.", Content="I love Bootstrap!", BlogBlogId=7 },
                new Post { Title="I am Tom.", Content="I love jQuery!", BlogBlogId=8 },
                new Post { Title="I am Rose.", Content="I love HTML5!", BlogBlogId=9 }
            };

            //將List加入到Entity集合
            using (var ctx = new BlogContext())
            {
                //檢查UserId為7的資料是否存在?若無則新增資料
                var user = ctx.Users.Find(7);
                if (user == null)
                {
                    ctx.Users.AddRange(users);
                    ctx.SaveChanges();   //呼叫SaveChanges()儲存異動

                    ctx.Blog.AddRange(blogs);
                    ctx.SaveChanges();

                    ctx.Post.AddRange(posts);
                    ctx.SaveChanges();
                }
                else
                {
                    Console.WriteLine("樣本資料己存在, 不新增資料");
                    return;
                }
            }

            Console.WriteLine("AddRange()執行完成,請按任意鍵離開...");
            Console.ReadKey();
        }

        //查詢並顯示資料
        static void DisplayData()
        {
            //這裡的db是指EF的DbContext,而非SQL Server的db資料庫
            using (var db = new BlogContext())
            {
                Console.WriteLine("\n顯示所有Users:");
                Console.WriteLine("==========================");

                //以LINQ查詢
                var allUsers = from u in db.Users
                               select u;

                foreach (var item in allUsers)
                {
                    Console.WriteLine($"{item.UserId}, {item.UserName}, {item.Email}");
                }

                Console.WriteLine("\n顯示某些條件的Users:");
                Console.WriteLine("==========================");

                //以LINQ查詢,過濾與排序
                var filter = from u in db.Users
                             where u.UserId >= 2 && u.UserId <= 5
                             orderby u.UserName descending
                             select u;

                foreach (var item in filter)
                {
                    Console.WriteLine($"{item.UserId}, {item.UserName}, {item.Email}");
                }

                Console.WriteLine("\n顯示指定的Users:");
                Console.WriteLine("==========================");

                var specificUsers = db.Users.ToList();


                //在ForEach()方法中做判斷
                specificUsers.ForEach(x =>
                {
                    if (x.UserName.Contains("祭司") || x.UserName == "Mary" || x.UserName == "John")
                    {
                        Console.WriteLine($"{x.UserId}, {x.UserName}, {x.Email}");
                    }
                });

                Console.WriteLine("\n顯示所有Blogs:");
                Console.WriteLine("==========================");

                var allBlogs = from b in db.Blog
                               select b;

                allBlogs.ToList().ForEach(b =>
                {
                    Console.WriteLine($"{b.BlogName}, {b.Url}, Owner: {b.User.UserName}");
                });

                Console.WriteLine("\n顯示所有Posts貼文:");
                Console.WriteLine("==========================");

                var allPosts = from u in db.Post
                               select u;

                allPosts.ToList().ForEach(p =>
                {
                    Console.WriteLine($"{p.PostId}, {p.Title}, {p.Content}, " +
                        $"BlogBlogId : {p.BlogBlogId}, BlogName: {p.Blog.BlogName}");
                });
            }

            Console.WriteLine("");
            Console.WriteLine("請按任意鍵離開...");
            Console.ReadKey();
        }
    }
}
