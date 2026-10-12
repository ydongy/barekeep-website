// Reads the release feed written by scripts/release.sh in the app repo and fills in the download button.
// The wording comes from data-* attributes on #download, written by scripts/build.py from i18n/<code>.json.
(function () {
  var box = document.getElementById("download");
  var status = document.getElementById("status");
  if (!box || !status) return;
  var d = box.dataset;
  function fill(s, v, os) { return s.replace("{v}", v).replace("{os}", os || ""); }
  fetch("https://dl.barekeep.com/latest.json", { cache: "no-store" })
    .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
    .then(function (f) {
      if (!/^https:\/\//.test(f.url)) throw new Error("bad url");
      status.textContent = fill(f.minimumOS ? d.version : d.versionNoOs, f.version, f.minimumOS);
      var a = document.getElementById("download-button");
      a.textContent = fill(d.button, f.version);
      a.href = f.url; a.hidden = false;
      if (f.sha256) {
        document.getElementById("sha").textContent = "SHA-256: " + f.sha256;
        document.getElementById("checksum").hidden = false;
      }
    })
    .catch(function () { status.textContent = d.error; });
})();
