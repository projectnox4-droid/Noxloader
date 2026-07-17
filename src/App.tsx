import React, { useState, useEffect, useRef } from 'react';
import { Terminal, Code2, ShieldAlert, Zap, Play, Flame, Search } from 'lucide-react';
import { motion, AnimatePresence } from 'motion/react';

type ScreenState = 'overview' | 'simulator';
type SimStep = 'menu' | 'checking' | 'available' | 'updating' | 'success' | 'reboot' | 'stalker_input' | 'stalker_monitoring';

export default function App() {
  const [screen, setScreen] = useState<ScreenState>('overview');
  const [simStep, setSimStep] = useState<SimStep>('menu');
  const [checkMsgIdx, setCheckMsgIdx] = useState(0);
  const [progress, setProgress] = useState(0);
  const [depStep, setDepStep] = useState(0);
  const [rebootProgress, setRebootProgress] = useState(0);
  const [rebootPhase, setRebootPhase] = useState(0);
  
  // Stalker state
  const [stalkerTarget, setStalkerTarget] = useState("");
  const [stalkerLogs, setStalkerLogs] = useState<string[]>([]);
  const [isPrivate, setIsPrivate] = useState(false);
  const logsEndRef = useRef<HTMLDivElement>(null);

  const checkMessages = [
    "😈 Ngecek update bentar...",
    "🗿 Nyambung ke GitHub...",
    "🥵 Nyari versi terbaru..."
  ];

  const depMessages = [
    "😈 Lagi nyiapin mesin...",
    "🗿 Update module...",
    "🥵 Sinkron dependency..."
  ];

  const getUpdateStatusText = (p: number) => {
    if (p < 20) return "😈 Lagi narik update...";
    if (p < 40) return "🗿 Nyusun file baru...";
    if (p < 60) return "🥵 Rapihin module...";
    if (p < 80) return "🤙 Bersihin cache...";
    return "😹 Hampir kelar...";
  };

  const renderProgressBar = (p: number, length = 14) => {
    const filled = Math.floor((p / 100) * length);
    const empty = length - filled;
    return "█".repeat(filled) + "░".repeat(empty);
  };

  // Checking sequence
  useEffect(() => {
    if (simStep === 'checking') {
      const interval = setInterval(() => {
        setCheckMsgIdx(prev => {
          if (prev >= checkMessages.length - 1) {
            clearInterval(interval);
            setTimeout(() => setSimStep('available'), 800);
            return prev;
          }
          return prev + 1;
        });
      }, 1000);
      return () => clearInterval(interval);
    }
  }, [simStep]);

  // Updating sequence
  useEffect(() => {
    if (simStep === 'updating') {
      setProgress(0);
      setDepStep(0);
      const interval = setInterval(() => {
        setProgress(p => {
          if (p >= 100) {
            clearInterval(interval);
            let dStep = 0;
            const depInt = setInterval(() => {
              dStep++;
              setDepStep(dStep);
              if (dStep >= 2) {
                clearInterval(depInt);
                setTimeout(() => setSimStep('success'), 1000);
              }
            }, 1000);
            return 100;
          }
          return p + 5;
        });
      }, 150);
      return () => clearInterval(interval);
    }
  }, [simStep]);

  // Success -> Reboot sequence
  useEffect(() => {
    if (simStep === 'success') {
      const t = setTimeout(() => {
        setSimStep('reboot');
        setRebootProgress(0);
        setRebootPhase(0);
      }, 3000);
      return () => clearTimeout(t);
    }
  }, [simStep]);

  // Reboot sequence
  useEffect(() => {
    if (simStep === 'reboot') {
      let interval: NodeJS.Timeout;
      if (rebootPhase === 0) {
        interval = setInterval(() => {
          setRebootProgress(p => {
            if (p >= 100) {
              clearInterval(interval);
              setTimeout(() => {
                setRebootPhase(1);
                setRebootProgress(0);
              }, 500);
              return 100;
            }
            return p + 10;
          });
        }, 100);
      } else if (rebootPhase === 1) {
        interval = setInterval(() => {
          setRebootProgress(p => {
            if (p >= 100) {
              clearInterval(interval);
              setTimeout(() => {
                setRebootPhase(2);
              }, 500);
              return 100;
            }
            return p + 10;
          });
        }, 100);
      }
      return () => clearInterval(interval);
    }
  }, [simStep, rebootPhase]);

  // Stalker simulation
  useEffect(() => {
    if (simStep === 'stalker_monitoring') {
      setStalkerLogs([`[+] Inisialisasi Stalker Mode untuk target: @${stalkerTarget}`, `[+] Mode Akun Private: ${isPrivate ? 'AKTIF (Risk: HIGH)' : 'NONAKTIF'}`]);
      
      const scenario = [
        { delay: 2000, msg: `[*] 🕵️ Memantau aktivitas @${stalkerTarget} (Interval: 10s)...` },
        { delay: 5000, msg: `[-] 💤 Belum ada pergerakan.` },
        { delay: 8000, msg: `[-] 💤 Belum ada pergerakan.` },
        { delay: 11000, msg: `[!] ⚠️ UPLOAD BARU TERDETEKSI! (Tipe: Story)` },
        { delay: 12000, msg: `[*] 📥 Mengunduh media: story_739281.mp4...` },
        { delay: 13500, msg: `[+] ✅ Berhasil! Tersimpan di /sdcard/Download/NoxLoader/@${stalkerTarget}/` },
        { delay: 16000, msg: `[*] 🕵️ Kembali memantau...` },
      ];

      const timeouts: NodeJS.Timeout[] = [];
      scenario.forEach(step => {
        const t = setTimeout(() => {
          setStalkerLogs(prev => [...prev, step.msg]);
        }, step.delay);
        timeouts.push(t);
      });

      return () => timeouts.forEach(t => clearTimeout(t));
    }
  }, [simStep, stalkerTarget, isPrivate]);

  useEffect(() => {
    if (logsEndRef.current) {
      logsEndRef.current.scrollIntoView({ behavior: 'smooth' });
    }
  }, [stalkerLogs]);

  const handleStartStalker = (e: React.FormEvent) => {
    e.preventDefault();
    if (stalkerTarget.trim()) {
      setSimStep('stalker_monitoring');
    }
  };

  return (
    <div className="min-h-screen bg-[#050505] font-mono text-[#00FFFF] flex flex-col items-center p-4 sm:p-8 selection:bg-[#00FFFF] selection:text-[#0a0a0a]">
      {screen === 'overview' && (
        <motion.div 
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          className="max-w-4xl w-full flex flex-col border-4 border-[#00FFFF] p-4 sm:p-6 bg-[#0a0a0a]"
        >
          <header className="flex flex-col sm:flex-row justify-between items-start mb-6 border-b border-[#00FFFF] pb-4">
            <div className="leading-none text-left">
              <pre className="text-[10px] sm:text-xs leading-[1.1] text-[#00FFFF] font-bold whitespace-pre">
{`███╗   ██╗ ██████╗ ██╗  ██╗
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

          <div className="border-2 border-[#00FFFF] p-4 sm:p-6 bg-[#0a0a0a] relative">
            <div className="absolute -top-3 left-4 bg-[#0a0a0a] px-2 text-xs font-bold uppercase flex items-center gap-2">
              ACTIVE_SESSION: SYSTEM_OVERVIEW
            </div>
            
            <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4 mb-6 mt-2 border-b border-[#004444] pb-4">
              <div className="flex items-center gap-3">
                <Terminal className="w-5 h-5 text-[#00FFFF]" />
                <h2 className="text-lg font-bold text-[#00FFFF]">Simulator UI Baru 🚀</h2>
              </div>
              <button 
                onClick={() => { setScreen('simulator'); setSimStep('menu'); }}
                className="bg-[#00FFFF] text-black px-4 py-2 text-sm font-bold flex items-center gap-2 hover:bg-white transition-colors uppercase"
              >
                <Play className="w-4 h-4" /> Buka Simulator CLI
              </button>
            </div>

            <p className="text-[#00FFFF] text-sm leading-relaxed mb-6 opacity-90">
              Sesuai request lu cok, ini fitur-fitur ngeri (termasuk fitur OP baru) udah gwe tanem langsung ke daleman <strong className="text-white">NOXLOADER</strong>:
              <br/><br/>
              <strong>1. Aria2c Multi-Threading</strong> (Nge-boost speed download 300% lebih gila, idupin di Setting)<br/>
              <strong>2. Intel Recon</strong> (Ngintip intel metadata asli dari link video tanpa perlu didownload)<br/>
              <strong>3. Auto-Update Engine</strong> (Update modul backend dengan 1 tombol, anti-basi)<br/>
              <strong>4. Auto-Resume & Speed Limit</strong> (Tahan banting kalau inet putus / set limit speed)<br/>
              <strong>5. Subtitle & Thumbnail Grabber</strong> (Auto comot takarir ID/EN & cover art)<br/>
              <strong>6. Custom Quality & Auto Metadata</strong> (Pilih resolusi, auto injek tagging MP3/MP4)<br/>
              <strong>7. Image/Album Bulk Scraper</strong> (Sedot foto IG, Pinterest, Twitter berjejer sekaligus)
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
                <li>noxloader/requirements.txt</li>
              </ul>
            </div>

            <div className="flex items-start gap-3 bg-[#001111] p-4 border border-[#004444] mb-6">
              <ShieldAlert className="w-5 h-5 text-[#00FFFF] shrink-0 mt-0.5" />
              <div className="text-sm text-[#00FFFF]">
                <strong className="block text-[#00FFFF] mb-1 uppercase font-bold">🔐 Fitur Baru: Auto Cookie Bypass (Anti Ribet)</strong>
                <div className="space-y-2 mt-2 opacity-90 text-xs">
                  <p>Udah gwe buatin <strong>Menu [8] Akses Private</strong> yang otomatis ngambil cookie dari keyboard/clipboard lu (Termux API).</p>
                </div>
              </div>
            </div>

            <div className="flex items-start gap-3 bg-[#110022] p-4 border border-[#8800ff] mb-6">
              <Zap className="w-5 h-5 text-[#cc00ff] shrink-0 mt-0.5" />
              <div className="text-sm text-[#eebbff]">
                <strong className="block text-[#cc00ff] mb-1 uppercase font-bold">🔮 UPDATE TERBARU: 11 Fitur OP Ngeri Udah Rilis! 😈</strong>
                <div className="space-y-2 mt-2 opacity-90 text-xs">
                  <p>NoxLoader sekarang makin gg gaming cok, 11 fitur super OP udah aktif di menu:</p>
                  <ul className="list-disc ml-4 space-y-1">
                    <li><strong>[10] 🔴 NOXSTREAM:</strong> Auto-record live streaming tanpa henti.</li>
                    <li><strong>[11] 🦇 Ngalong Mode:</strong> Auto-download jam 2 pagi pas kuota malam idup.</li>
                    <li><strong>[12] 👻 Ghost Mode:</strong> Nyamar pake Proxy/Tor rotator anti banned IP.</li>
                    <li><strong>[13] 🎧 NOXAUDIO:</strong> Sedot Spotify, Soundcloud, & Apple Music format FLAC/320kbps.</li>
                    <li><strong>[14] ✂️ Auto-Cutter:</strong> Potong & trim video langsung dari terminal pake FFmpeg.</li>
                    <li><strong>[15] 🔞 Premium Scraper:</strong> Sedot se-folder OnlyFans/Drive (Wajib auto-cookie Menu 8).</li>
                    <li><strong>[16] 🖼️ Image Scraper:</strong> Sedot album foto IG/Pinterest/Twitter sekaligus.</li>
                    <li><strong>[17] ☁️ Cloud Forwarder:</strong> Habis download otomatis forward ke Telegram Bot / Google Drive.</li>
                    <li><strong>[18] 🧲 Magnet Engine:</strong> Sedot link Torrent / Magnet langsung jadi file mateng.</li>
                    <li><strong>[19] 🎬 Auto-Meme (GIF Maker):</strong> Convert video ke WebP/GIF buat stiker.</li>
                    <li><strong>[20] 📚 Batch TXT Injector:</strong> Auto-download massal ribuan link dari file .txt.</li>
                  </ul>
                </div>
              </div>
            </div>

            <div className="flex items-start gap-3 bg-[#220011] p-4 border border-[#ff0044] mb-6">
              <Flame className="w-5 h-5 text-[#ff0044] shrink-0 mt-0.5" />
              <div className="text-sm text-[#ff99bb]">
                <strong className="block text-[#ff0044] mb-1 uppercase font-bold">🔥 FITUR SPESIAL: STALKER MODE</strong>
                <div className="space-y-2 mt-2 opacity-90 text-xs">
                  <p><strong>🕵️ Stalker Mode:</strong> Masukin username IG/TikTok target (crush, musuh). Tiap dia bikin Story/Reels baru, otomatis kesedot ke HP lu 24/7 (cronjob)! Dilengkapi fitur bypass Akun Private. Udah bisa dicoba di Simulator CLI (Pilih Menu 21).</p>
                </div>
              </div>
            </div>

          </div>

          <footer className="mt-6 bg-[#00FFFF] text-[#0a0a0a] px-4 py-2 text-[10px] font-bold flex justify-between uppercase w-full">
            <span>100% Python • Termux Native</span>
            <span className="hidden sm:inline">No Raw Outputs • Fully Wrapped</span>
            <span>🗿 Guest_Nox</span>
          </footer>
        </motion.div>
      )}

      {screen === 'simulator' && (
        <motion.div 
          initial={{ opacity: 0, scale: 0.95 }}
          animate={{ opacity: 1, scale: 1 }}
          exit={{ opacity: 0 }}
          className="max-w-3xl w-full flex flex-col border border-[#004444] bg-[#000000] p-4 font-mono text-sm shadow-[0_0_20px_rgba(0,255,255,0.1)]"
        >
          {/* Mock CLI Header */}
          <div className="text-[#00FFFF] mb-6 font-bold flex justify-between border-b border-[#004444] pb-2">
            <div>
              <span className="text-[#008888]">guest@termux:</span><span className="text-[#004444]">~</span>$ python main.py
            </div>
            <button 
              onClick={() => setScreen('overview')}
              className="text-[#008888] hover:text-[#00FFFF] underline text-xs uppercase"
            >
              [X] Close Simulator
            </button>
          </div>

          <div className="flex-1 min-h-[400px]">
            <AnimatePresence mode="wait">
              {simStep === 'menu' && (
                <motion.div key="menu" initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}>
                  <pre className="text-[#00FFFF] font-bold text-xs sm:text-sm mb-4">
{`███╗   ██╗ ██████╗ ██╗  ██╗
████╗  ██║██╔═══██╗╚██╗██╔╝
██╔██╗ ██║██║   ██║ ╚███╔╝ 
██║╚██╗██║██║   ██║ ██╔██╗ 
██║ ╚████║╚██████╔╝██╔╝ ██╗
╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝
LOADER v2.4.1`}
                  </pre>
                  <div className="space-y-1 text-[#00FFFF]">
                    <p>[1] Download Video / Playlist</p>
                    <p>[2] Download Audio Only</p>
                    <p className="text-[#008888]">...</p>
                    <p>[16] 🖼️ Image Bulk Scraper</p>
                    <p>[17] ☁️ Cloud Forwarder</p>
                    <p>[18] 🧲 Magnet Engine</p>
                    <p>[19] 🎬 Auto-Meme (GIF Maker)</p>
                    <p>[20] 📚 Batch TXT Injector</p>
                    <p className="text-[#ff0044] font-bold">[21] 🕵️ Stalker Mode (Profile Monitor)</p>
                    <p className="text-yellow-400 font-bold">[22] 🔄 Update NOXLOADER</p>
                    <p>[0] Exit</p>
                    <div className="mt-4 flex items-center gap-4">
                      <span>{">"}</span>
                      <button 
                        onClick={() => {
                          setSimStep('stalker_input');
                        }}
                        className="bg-[#ff0044] text-white px-2 hover:bg-white hover:text-black font-bold"
                      >
                        21 (Stalker)
                      </button>
                      <button 
                        onClick={() => {
                          setCheckMsgIdx(0);
                          setSimStep('checking');
                        }}
                        className="animate-pulse bg-[#00FFFF] text-black px-2 hover:bg-white font-bold"
                      >
                        22 (Update)
                      </button>
                    </div>
                  </div>
                </motion.div>
              )}

              {simStep === 'stalker_input' && (
                <motion.div key="stalker_input" initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}>
                  <div className="text-[#00FFFF] space-y-4">
                    <pre className="text-[#ff0044] font-bold text-xs sm:text-sm">
{`   _____ __        ____             
  / ___// /_____ _/ / /_____  _____ 
  \\__ \\/ __/ __ \`/ / //_/ _ \\/ ___/ 
 ___/ / /_/ /_/ / / ,< /  __/ /     
/____/\\__/\\__,_/_/_/|_|\\___/_/      
           MODE: ACTIVE`}
                    </pre>
                    <p className="text-[#ff99bb] border-l-2 border-[#ff0044] pl-2 text-xs">
                      Fitur ini akan memantau target 24/7 di background.
                      Setiap ada unggahan Story, Reels, atau Feed baru,
                      NoxLoader akan otomatis mengunduh ke storage lokal.
                    </p>

                    <form onSubmit={handleStartStalker} className="space-y-4 mt-6 border border-[#004444] p-4 bg-[#0a0a0a]">
                      <div>
                        <label className="block text-xs mb-1 text-[#008888]">Username Target (tanpa @):</label>
                        <div className="flex items-center gap-2">
                          <span className="text-[#00FFFF] font-bold">@</span>
                          <input 
                            type="text"
                            required
                            value={stalkerTarget}
                            onChange={(e) => setStalkerTarget(e.target.value)}
                            className="bg-transparent border-b border-[#00FFFF] focus:outline-none focus:border-white text-white px-1 w-full max-w-[200px]"
                            placeholder="username..."
                          />
                        </div>
                      </div>

                      <div className="pt-2">
                        <label className="flex items-start gap-2 cursor-pointer group">
                          <input 
                            type="checkbox"
                            checked={isPrivate}
                            onChange={(e) => setIsPrivate(e.target.checked)}
                            className="mt-1 accent-[#ff0044]"
                          />
                          <div>
                            <span className="block text-sm font-bold text-yellow-400 group-hover:text-yellow-300">Intip Akun Private (Private Bypass)</span>
                            <span className="block text-[10px] text-gray-500 mt-1">Wajib sudah inject cookie di Menu [8]. Warning: Risiko ban akun IG tumbal lebih tinggi jika interval terlalu cepat.</span>
                          </div>
                        </label>
                      </div>

                      <div className="pt-4 flex gap-3">
                        <button 
                          type="submit"
                          className="bg-[#ff0044] text-white font-bold px-4 py-1 flex items-center gap-2 hover:bg-white hover:text-black transition-colors"
                        >
                          <Search className="w-4 h-4" /> Start Monitoring
                        </button>
                        <button 
                          type="button"
                          onClick={() => setSimStep('menu')}
                          className="border border-[#008888] text-[#008888] font-bold px-4 py-1 hover:bg-[#004444] transition-colors"
                        >
                          Batal
                        </button>
                      </div>
                    </form>
                  </div>
                </motion.div>
              )}

              {simStep === 'stalker_monitoring' && (
                <motion.div key="stalker_monitoring" initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}>
                  <div className="flex justify-between items-center mb-4 border-b border-[#004444] pb-2">
                    <span className="font-bold text-[#ff0044] animate-pulse">🔴 LIVE MONITORING</span>
                    <button 
                      onClick={() => setSimStep('menu')}
                      className="text-xs border border-[#008888] px-2 py-0.5 hover:bg-[#004444]"
                    >
                      [CTRL+C] Stop
                    </button>
                  </div>
                  
                  <div className="space-y-1 text-xs sm:text-sm font-mono h-[300px] overflow-y-auto pr-2 custom-scrollbar">
                    {stalkerLogs.map((log, i) => {
                      let color = "text-gray-300";
                      if (log.includes("[+]") || log.includes("✅")) color = "text-green-400 font-bold";
                      else if (log.includes("[-]")) color = "text-gray-500";
                      else if (log.includes("[!]") || log.includes("⚠️")) color = "text-yellow-400 font-bold";
                      else if (log.includes("[*]")) color = "text-[#00FFFF]";

                      return (
                        <motion.div 
                          key={i}
                          initial={{ opacity: 0, x: -5 }}
                          animate={{ opacity: 1, x: 0 }}
                          className={color}
                        >
                          {log}
                        </motion.div>
                      );
                    })}
                    <div ref={logsEndRef} />
                  </div>
                </motion.div>
              )}

              {simStep === 'checking' && (
                <motion.div key="checking" initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}>
                  <div className="space-y-2 text-[#00FFFF]">
                    {checkMessages.slice(0, checkMsgIdx + 1).map((msg, i) => (
                      <motion.div 
                        key={i}
                        initial={{ x: -10, opacity: 0 }}
                        animate={{ x: 0, opacity: 1 }}
                      >
                        {msg} {i === checkMsgIdx && <span className="animate-pulse">_</span>}
                      </motion.div>
                    ))}
                  </div>
                </motion.div>
              )}

              {simStep === 'available' && (
                <motion.div key="available" initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}>
                  <div className="text-[#00FFFF]">
                    <p>━━━━━━━━━━━━━━━━━━━━</p>
                    <p className="font-bold text-yellow-400 my-2">😈 Update ketemu.</p>
                    <p className="text-gray-400">Versi sekarang:</p>
                    <p className="font-bold">v2.4.1</p>
                    <p className="my-1">↓</p>
                    <p className="text-gray-400">Versi terbaru:</p>
                    <p className="font-bold text-green-400">v2.5.0</p>
                    <p>━━━━━━━━━━━━━━━━━━━━</p>
                    
                    <div className="flex gap-4 mt-4">
                      <button 
                        onClick={() => setSimStep('updating')}
                        className="bg-[#00FFFF] text-black font-bold px-4 py-1 hover:bg-white"
                      >
                        [ Update ]
                      </button>
                      <button 
                        onClick={() => setSimStep('menu')}
                        className="border border-[#00FFFF] text-[#00FFFF] font-bold px-4 py-1 hover:bg-[#004444]"
                      >
                        [ Batal ]
                      </button>
                    </div>
                  </div>
                </motion.div>
              )}

              {simStep === 'updating' && (
                <motion.div key="updating" initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}>
                  <div className="space-y-4">
                    {progress < 100 && (
                      <div className="text-[#00FFFF]">
                        <p className="mb-2">{getUpdateStatusText(progress)}</p>
                        <p className="text-lg tracking-widest">{renderProgressBar(progress, 20)} {progress}%</p>
                      </div>
                    )}
                    
                    {progress >= 100 && (
                      <div className="space-y-2 text-[#00FFFF]">
                        {depMessages.slice(0, depStep + 1).map((msg, i) => (
                          <motion.div 
                            key={i}
                            initial={{ x: -10, opacity: 0 }}
                            animate={{ x: 0, opacity: 1 }}
                          >
                            {msg} {i === depStep && <span className="animate-pulse">_</span>}
                          </motion.div>
                        ))}
                      </div>
                    )}
                  </div>
                </motion.div>
              )}

              {simStep === 'success' && (
                <motion.div key="success" initial={{ opacity: 0, scale: 0.9 }} animate={{ opacity: 1, scale: 1 }} exit={{ opacity: 0 }}>
                  <pre className="text-green-400 font-bold inline-block whitespace-pre">
{`╭━━━━━━━━━━━━━━━━━━╮
│ 😹 UPDATE DONE   │
│                  │
│ NOXLOADER READY  │
│                  │
│ Version v2.5.0   │
╰━━━━━━━━━━━━━━━━━━╯`}
                  </pre>
                </motion.div>
              )}

              {simStep === 'reboot' && (
                <motion.div key="reboot" initial={{ opacity: 0 }} animate={{ opacity: 1 }}>
                  <div className="text-[#00FFFF] space-y-2">
                    <p className="font-bold">NOXLOADER STARTING...</p>
                    
                    {rebootPhase >= 0 && (
                      <div>
                        <p>Checking module...</p>
                        <p className="tracking-widest">{renderProgressBar(rebootPhase > 0 ? 100 : rebootProgress, 12)} {rebootPhase > 0 ? 100 : rebootProgress}%</p>
                      </div>
                    )}
                    
                    {rebootPhase >= 1 && (
                      <div className="mt-2">
                        <p>Loading system...</p>
                        <p className="tracking-widest">{renderProgressBar(rebootPhase > 1 ? 100 : rebootProgress, 12)} {rebootPhase > 1 ? 100 : rebootProgress}%</p>
                      </div>
                    )}

                    {rebootPhase >= 2 && (
                      <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="mt-4">
                        <p className="text-gray-400">Version:</p>
                        <p className="font-bold text-green-400">v2.5.0</p>
                        <p className="font-bold text-[#00FFFF] mt-2">SYSTEM READY</p>
                        
                        <div className="mt-4">
                          <button 
                            onClick={() => setSimStep('menu')}
                            className="bg-[#00FFFF] text-black px-4 py-1 hover:bg-white font-bold"
                          >
                            [Enter] Balik ke menu...
                          </button>
                        </div>
                      </motion.div>
                    )}
                  </div>
                </motion.div>
              )}
            </AnimatePresence>
          </div>
        </motion.div>
      )}
      <style dangerouslySetInnerHTML={{__html: `
        .custom-scrollbar::-webkit-scrollbar {
          width: 6px;
        }
        .custom-scrollbar::-webkit-scrollbar-track {
          background: #001111; 
        }
        .custom-scrollbar::-webkit-scrollbar-thumb {
          background: #008888; 
        }
        .custom-scrollbar::-webkit-scrollbar-thumb:hover {
          background: #00FFFF; 
        }
      `}} />
    </div>
  );
}
