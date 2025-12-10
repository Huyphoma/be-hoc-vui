import "../styles/globals.css";

export default function MyApp({ Component, pageProps }) {
  return (
    <div className="bhv-shell">
      <div className="bhv-gradient-ring" />
      <header className="bhv-nav">
        <div className="bhv-nav-inner">
          <a href="/" className="bhv-logo">
            <div className="bhv-logo-mark">Bé</div>
            <div>
              <div className="bhv-logo-text-main">Bé Học Vui</div>
              <div className="bhv-logo-text-sub">Học mà chơi · Chơi mà học</div>
            </div>
          </a>
          <div className="bhv-chip">
            <span style={{ width: 8, height: 8, borderRadius: 999, background: "#22c55e" }} />
            Mục tiêu 1.000.000 bé · 2026
          </div>
        </div>
      </header>
      <main className="bhv-main">
        <div className="bhv-main-inner">
          <Component {...pageProps} />
        </div>
      </main>
    </div>
  );
}
