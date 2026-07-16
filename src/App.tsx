/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import { Terminal, Download, Code2, ShieldAlert } from "lucide-react";

export default function App() {
  return (
    <div className="min-h-screen bg-[#0a0a0a] text-[#00FFFF] font-mono flex flex-col items-center p-4 sm:p-8 selection:bg-[#00FFFF] selection:text-[#0a0a0a]">
      <div className="max-w-4xl w-full flex flex-col border-4 border-[#00FFFF] p-4 sm:p-6 bg-[#0a0a0a]">
        <header className="flex flex-col sm:flex-row justify-between items-start mb-6 border-b border-[#00FFFF] pb-4 animate-in fade-in slide-in-from-top-4 duration-1000">
          <div className="leading-none text-left">
            <pre className="text-[10px] sm:text-xs leading-[1.1] text-[#00FFFF] font-bold">
              {`
███╗   ██╗ ██████╗ ██╗  ██╗
████╗  ██║██╔═══██╗╚██╗██╔╝
██╔██╗ ██║██║   ██║ ╚███╔╝
██║╚██╗██║██║   ██║ ██╔██╗
██║ ╚████║╚██████╔╝██╔╝ ██╗
╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝
            LOADER`}
            </pre>
            <h1 className="text-xl sm:text-2xl font-bold tracking-widest text-[#00FFFF] uppercase mt-4">
              NOXLOADER
            </h1>
            <p className="text-[#00FFFF] tracking-widest text-xs sm:text-sm uppercase mt-1 opacity-80">AUTO SMART UNIVERSAL DOWNLOADER</p>
          </div>
          <div className="hidden sm:block text-right text-xs space-y-1 mt-4 sm:mt-0 opacity-80">
            <p>😈 STATUS: <span className="text-green-400">CONNECTED</span></p>
            <p>🗿 DIR: /sdcard/Download/NoxLoader/</p>
            <p>🤙 TERMINAL: TERMUX_A14</p>
          </div>
        </header>

        <div className="border-2 border-[#00FFFF] p-4 sm:p-6 bg-[#0a0a0a] relative animate-in fade-in slide-in-from-bottom-6 duration-1000 delay-150">
          <div className="absolute -top-3 left-4 bg-[#0a0a0a] px-2 text-xs font-bold uppercase">ACTIVE_SESSION: SYSTEM_OVERVIEW</div>
          
          <div className="flex items-center gap-3 mb-4 mt-2">
            <Terminal className="w-5 h-5 text-[#00FFFF]" />
            <h2 className="text-lg font-bold text-[#00FFFF]">6 Fitur Dewa Activated 🔥</h2>
          </div>
          <p className="text-[#00FFFF] text-sm leading-relaxed mb-6 opacity-90">
            Sesuai request lu cok, ini 6 fitur ngeri udah gwe tanem langsung ke daleman <strong className="text-white">NOXLOADER</strong>:
            <br/><br/>
            <strong>1. Auto-Resume & Retry</strong> (Tahan banting kalau inet putus)<br/>
            <strong>2. Speed Limit</strong> (Biar nggak nyedot kuota, setel di Pengaturan)<br/>
            <strong>3. Subtitle Grabber</strong> (Auto comot takarir ID/EN)<br/>
            <strong>4. Thumbnail Grabber</strong> (Download cover sampulnya juga)<br/>
            <strong>5. Auto Metadata Injector</strong> (Tagging artis/judul rapih)<br/>
            <strong>6. Custom Quality</strong> (Bisa pilih 1080p, 720p, 480p pas mau download video)
          </p>

          <div className="bg-[#001111] p-4 border border-[#004444] font-mono text-xs text-[#00FFFF] mb-6">
            <div className="flex items-center gap-2 mb-2 text-[#00FFFF] opacity-80 border-b border-[#004444] pb-2">
              <Code2 className="w-4 h-4" />
              <span>Struktur Folder Python (Cek menu Explorer/Code)</span>
            </div>
            <ul className="space-y-1 ml-6 list-disc marker:text-[#00FFFF] pt-2 opacity-90">
              <li>noxloader/main.py</li>
              <li>noxloader/core/menu.py</li>
              <li>noxloader/downloader/engine.py (Smart Queue)</li>
              <li>noxloader/ui/banner.py, theme.py, animations.py</li>
              <li>noxloader/utils/installer.py, scanner.py, cleaner.py</li>
              <li>noxloader/history/manager.py</li>
              <li>noxloader/config/settings.py</li>
              <li>noxloader/requirements.txt</li>
            </ul>
          </div>

          <div className="flex items-start gap-3 bg-[#001111] p-4 border border-[#004444] mb-6">
            <ShieldAlert className="w-5 h-5 text-[#00FFFF] shrink-0 mt-0.5" />
            <div className="text-sm text-[#00FFFF]">
              <strong className="block text-[#00FFFF] mb-1 uppercase font-bold">🔐 Fitur Baru: Auto Cookie Bypass (Anti Ribet)</strong>
              <div className="space-y-2 mt-2 opacity-90 text-xs">
                <p>Udah gwe buatin <strong>Menu [8] Akses Private</strong> yang otomatis ngambil cookie dari keyboard/clipboard lu (Termux API). Gini cara pakenya:</p>
                <ol className="list-decimal ml-4 space-y-1">
                  <li>Install ekstensi <strong>Get cookies.txt LOCALLY</strong> di Kiwi Browser / Yandex / Chrome PC.</li>
                  <li>Login ke IG/YT/FB pake akun lu, terus <strong>Copy semua isi cookie</strong> pake ekstensi tadi.</li>
                  <li>Masuk ke NoxLoader, pilih <strong>Menu 8</strong>.</li>
                  <li>Gwe bakal otomatis baca keyboard lu, nyimpen cookie nya, dan langsung minta link video private nya.</li>
                  <li><em>Catatan:</em> Lu wajib install aplikasi <strong>Termux:API</strong> dari PlayStore/F-Droid biar gwe bisa baca keyboard lu!</li>
                </ol>
              </div>
            </div>
          </div>

          <div className="flex items-start gap-3 bg-[#002222] p-4 border border-[#00FFFF]">
            <Terminal className="w-5 h-5 text-[#00FFFF] shrink-0 mt-0.5" />
            <div className="text-sm text-[#00FFFF]">
              <strong className="block text-[#00FFFF] mb-1 uppercase font-bold">Cara Pake di Termux HP Lu:</strong>
              <div className="space-y-1 mt-2 opacity-90">
                <div>1. Download project ini lewat menu <strong className="text-white">Settings (Logo Gear) &gt; Export as ZIP</strong>.</div>
                <div>2. Ekstrak di storage internal HP lu.</div>
                <div>3. Buka Termux, masuk ke foldernya: <code className="bg-[#0a0a0a] border border-[#004444] px-1.5 py-0.5 text-xs">cd /sdcard/noxloader</code></div>
                <div>4. Ketik <code className="bg-[#0a0a0a] border border-[#004444] px-1.5 py-0.5 text-xs">python main.py</code> dan santuy. 😈</div>
              </div>
            </div>
          </div>
        </div>

        <footer className="mt-6 bg-[#00FFFF] text-[#0a0a0a] px-4 py-2 text-[10px] font-bold flex justify-between uppercase italic w-full animate-in fade-in duration-1000 delay-300">
          <span>100% Python • Termux Native</span>
          <span className="hidden sm:inline">No Raw Outputs • Fully Wrapped</span>
          <span>🗿 Guest_Nox</span>
        </footer>
      </div>
    </div>
  );
}
