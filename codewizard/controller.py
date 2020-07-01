import web

urls = (
    '/', 'home'
)

app = web.application(urls, globals())

# classes/ Routs

class home:
    def GET(self):
        return "home"

if __name__ == "__main__":
    app.run()
