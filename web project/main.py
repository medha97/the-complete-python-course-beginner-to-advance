import web

urls = (
    '/(.*)','index'
)

app = web.application(urls, globals())

class index:
    def GET(self, name):
        return "<h1>hello " + name + ".</h1> How are you today?"

if __name__ =="__main__":
    app.run()
