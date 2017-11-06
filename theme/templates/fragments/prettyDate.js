    <script>
      function prettyDate(time) {
        var date = new Date((time || "").replace(/-/g, "/").replace(/[TZ]/g, " ")),
            dd = Math.floor((((new Date()).getTime() - date.getTime()) / 1000) / 86400), y = date.getFullYear(), m = date.getMonth()+1, d = date.getDate();
        if (isNaN(dd) || dd < 0 || dd >= 31)
            return (y.toString()+'-'+((m<10) ? '0'+m.toString() : m.toString())+'-'+((d<10) ? '0'+d.toString() : d.toString()));
        var r = ((dd == 0 && "Today") || (dd == 1 && "Yesterday") || (dd < 7 && dd + " days") || (dd < 31 && ( (dd < 14 && "1 week") || (dd < 21 && "2 weeks") || (dd < 28 && "3 weeks") || (dd < 25 && "4 weeks") ) ) );
        if (dd > 7 && dd % 7) r += " & " + dd % 7 + " days"
        return r;
      }
      document.addEventListener("DOMContentLoaded", function () { updateTimes(); setInterval(updateTimes, 60000);})
      function updateTimes() {
        var times = document.querySelectorAll("time");
        for (var i = 0; i < times.length; i++) {
          var s = prettyDate(times[i].getAttribute("datetime"));
          if (s) times[i].innerHTML = s
        }
      }
    </script>
