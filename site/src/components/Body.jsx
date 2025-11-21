import { useState, useEffect, useRef } from "react";
import Content from "./Content";

function Body() {
    const [authUser, setAuthUser] = useState(null);
    const [showExplorer, setShowExplorer] = useState(false);
    const [mountCloudStorage, setMountCloudStorage] = useState(false);
    const [fileTree, setFileTree] = useState([]);
    const [loading, setLoading] = useState(false);
    const [explorerWidth, setExplorerWidth] = useState(250);
    const [isResizing, setIsResizing] = useState(false);
    const explorerRef = useRef(null);
    
    useEffect(() => {
        fetch('http://localhost:3000/me', { credentials: 'include' })
            .then(r => r.ok ? r.json() : null)
            .then(data => setAuthUser(data))
            .catch(() => setAuthUser(null));
    }, []);
    useEffect(() => {
        const handleMessage = (event) => {
            if (event.origin !== 'http://localhost:3000') return;
            
            if (event.data.type === 'GOOGLE_DRIVE_CONNECTED' && event.data.success) {
                setMountCloudStorage(true);
                setShowExplorer(true);
                loadFileTree();
            }
        };

        window.addEventListener('message', handleMessage);
        return () => window.removeEventListener('message', handleMessage);
    }, []);

    // Logic xử lý resize - thanh resize di chuyển theo chuột
    useEffect(() => {
        const handleMouseMove = (e) => {
            if (!isResizing) return;

            const mouseX = e.clientX;
            const sidebarWidth = 50; // width of .Side_bar

            const minWidth = 250;
            const maxWidth = 500;

            const desired = mouseX - sidebarWidth;
            const clamped = Math.max(minWidth, Math.min(maxWidth, desired));
            setExplorerWidth(clamped);
        };

        const handleMouseUp = () => {
            setIsResizing(false);
        };

        if (isResizing) {
            document.addEventListener("mousemove", handleMouseMove);
            document.addEventListener("mouseup", handleMouseUp);
        }

        return () => {
            document.removeEventListener("mousemove", handleMouseMove);
            document.removeEventListener("mouseup", handleMouseUp);
        };
    }, [isResizing]);

    const handleResizeStart = (e) => {
        e.preventDefault();
        setIsResizing(true);
    };

    const loadFileTree = async () => {
        setLoading(true);
        
        const minLoadingTime = new Promise(resolve => setTimeout(resolve, 1000));
        
        try {
            const response = await fetch('http://localhost:3000/drive/files', {
                credentials: 'include'
            });
            
            if (response.ok) {
                const tree = await response.json();
                setFileTree(tree);
            } else {
                console.error('Failed to load file tree');
            }
        } catch (error) {
            console.error('Error loading file tree:', error);
        } finally {
            await minLoadingTime;
            setLoading(false);
        }
    };

    // Component để render file tree
    const FileTreeItem = ({ file, level = 0 }) => {
        const [isExpanded, setIsExpanded] = useState(false);
        const hasChildren = file.children && file.children.length > 0;
        const isFolder = file.isFolder;

        return (
            <div style={{ marginLeft: `${level * 20}px` }}>
                <div 
                    className="file-item"
                    style={{ 
                        display: 'flex', 
                        alignItems: 'center', 
                        padding: '4px 8px',
                        cursor: isFolder ? 'pointer' : 'default',
                    }}
                    onClick={() => isFolder && setIsExpanded(!isExpanded)}
                >
                    {isFolder && (
                        <span>
                            {isExpanded ? (<svg xmlns="http://www.w3.org/2000/svg" height="20px" viewBox="0 -960 960 960" width="20px" fill="#666666"><path d="M480-384 288-576h384L480-384Z"/></svg>) : (<svg xmlns="http://www.w3.org/2000/svg" height="20px" viewBox="0 -960 960 960" width="20px" fill="#666666"><path d="M384-288v-384l192 192-192 192Z"/></svg>)}
                        </span>
                    )}
                    {isFolder && (
                        <span style={{ marginRight: '8px' }}>
                            {isExpanded ? 
                            (<svg xmlns="http://www.w3.org/2000/svg" height="20px" viewBox="0 -960 960 960" width="20px" fill="#666666">
                                <path d="M168-192q-32 0-52-21t-20-51v-432q0-30 20-51t52-21h216l96 96h313q31 0 50.5 21t21.5 51H168v336l78-264h690l-85 285q-8 23-21 37t-38 14H168Z"/>
                            </svg>) : 
                            (<svg xmlns="http://www.w3.org/2000/svg" height="20px" viewBox="0 -960 960 960" width="20px" fill="#666666">
                                <path d="M168-192q-29 0-50.5-21.5T96-264v-432q0-30 21.5-51t50.5-21h216l96 96h312q30 0 51 21t21 51v336q0 29-21 50.5T792-192H168Z"/>
                            </svg>)}
                        </span>
                    )}
                    {!isFolder && 
                        <span style={{ marginRight: '8px' }}>
                            <svg xmlns="http://www.w3.org/2000/svg" height="20px" viewBox="0 -960 960 960" width="20px" fill="#666666">
                                <path d="M336-240h288v-72H336v72Zm0-144h288v-72H336v72ZM263.72-96Q234-96 213-117.15T192-168v-624q0-29.7 21.15-50.85Q234.3-864 264-864h312l192 192v504q0 29.7-21.16 50.85Q725.68-96 695.96-96H263.72ZM528-624h168L528-792v168Z"/>
                            </svg>
                        </span>}
                    <span style={{ flex: 1 }}>{file.name}</span>
                </div>
                {isExpanded && hasChildren && (
                    <div>
                        {file.children.map(child => (
                            <FileTreeItem key={child.id} file={child} level={level + 1} />
                        ))}
                    </div>
                )}
            </div>
        );
    };
    

// Hàm tạo file bất kỳ
const createAnyFile = async () => {
    const fileName = prompt('Enter file name (with extension, e.g., "myfile.txt", "document.html"):');
    if (!fileName) return;

    // Xác định file type từ extension
    const extension = fileName.split('.').pop()?.toLowerCase() || 'txt';
    
    try {
        const response = await fetch('http://localhost:3000/drive/files/create', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            credentials: 'include',
            body: JSON.stringify({ 
                fileName: fileName,
                fileType: extension,
                content: `This is a new ${extension} file created at ${new Date().toLocaleString()}`
            })
        });

        if (response.ok) {
            const result = await response.json();
            console.log('File created:', result);
            alert(result.message);
            // Reload file tree để hiển thị file mới
            loadFileTree();
        } else {
            const error = await response.json();
            console.error('Error creating file:', error);
            alert(`Error: ${error.message}`);
        }
    } catch (error) {
        console.error('Error creating file:', error);
        alert('Error creating file');
    }
};

    return (
        <div className={`Body ${isResizing ? 'resizing' : ''}`}>
            {authUser ? (
                <>
                <div className="Side_bar"> 
                    <button className={showExplorer ? "File_explorer onselect" : "File_explorer"} onClick={() => setShowExplorer(v => !v)}>                  
                        <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1e453e">
                            <path d="M160-160q-33 0-56.5-23.5T80-240v-480q0-33 23.5-56.5T160-800h240l80 80h320q33 0 56.5 23.5T880-640H447l-80-80H160v480l96-320h684L837-217q-8 26-29.5 41.5T760-160H160Zm84-80h516l72-240H316l-72 240Zm0 0 72-240-72 240Zm-84-400v-80 80Z"/>
                        </svg>                    
                    </button> 
                </div>
                {showExplorer && (
                        <div className="Explorer_panel" ref={explorerRef} style={{ width: `${explorerWidth}px` }}>
                            <div className="Explorer_panel_title">
                                <span> File Explorer </span>
                                <button className="Close_panel_button" onClick={() => setShowExplorer(v => !v)}>
                                    <svg xmlns="http://www.w3.org/2000/svg" height="25px" viewBox="0 -960 960 960" width="25px" fill="#1e453e">
                                        <path d="M440-240 200-480l240-240 56 56-183 184 183 184-56 56Zm264 0L464-480l240-240 56 56-183 184 183 184-56 56Z"/>
                                    </svg>
                                </button>
                            </div>
                            {mountCloudStorage ? (      
                                <div className="Container_1">                     
                                    <div className="File_tree_button">
                                        <button>
                                            <svg width="20px" height="20px" viewBox="0 0 24 24" fill=" #1e453e" stroke=" #1e453e" stroke-width="0.25" xmlns="http://www.w3.org/2000/svg">
                                                <path d="M12.5535 2.49392C12.4114 2.33852 12.2106 2.25 12 2.25C11.7894 2.25 11.5886 2.33852 11.4465 2.49392L7.44648 6.86892C7.16698 7.17462 7.18822 7.64902 7.49392 7.92852C7.79963 8.20802 8.27402 8.18678 8.55352 7.88108L11.25 4.9318V16C11.25 16.4142 11.5858 16.75 12 16.75C12.4142 16.75 12.75 16.4142 12.75 16V4.9318L15.4465 7.88108C15.726 8.18678 16.2004 8.20802 16.5061 7.92852C16.8118 7.64902 16.833 7.17462 16.5535 6.86892L12.5535 2.49392Z" fill="#1C274C"/>
                                                <path d="M3.75 15C3.75 14.5858 3.41422 14.25 3 14.25C2.58579 14.25 2.25 14.5858 2.25 15V15.0549C2.24998 16.4225 2.24996 17.5248 2.36652 18.3918C2.48754 19.2919 2.74643 20.0497 3.34835 20.6516C3.95027 21.2536 4.70814 21.5125 5.60825 21.6335C6.47522 21.75 7.57754 21.75 8.94513 21.75H15.0549C16.4225 21.75 17.5248 21.75 18.3918 21.6335C19.2919 21.5125 20.0497 21.2536 20.6517 20.6516C21.2536 20.0497 21.5125 19.2919 21.6335 18.3918C21.75 17.5248 21.75 16.4225 21.75 15.0549V15C21.75 14.5858 21.4142 14.25 21 14.25C20.5858 14.25 20.25 14.5858 20.25 15C20.25 16.4354 20.2484 17.4365 20.1469 18.1919C20.0482 18.9257 19.8678 19.3142 19.591 19.591C19.3142 19.8678 18.9257 20.0482 18.1919 20.1469C17.4365 20.2484 16.4354 20.25 15 20.25H9C7.56459 20.25 6.56347 20.2484 5.80812 20.1469C5.07435 20.0482 4.68577 19.8678 4.40901 19.591C4.13225 19.3142 3.9518 18.9257 3.85315 18.1919C3.75159 17.4365 3.75 16.4354 3.75 15Z" fill="#1C274C"/>
                                            </svg>
                                        </button>
                                        <button onClick={createAnyFile} >
                                            <svg width="20px" height="20px" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg" fill=" #1e453e" stroke=" #1e453e" stroke-width="0.25">
                                                <path fill-rule="evenodd" clip-rule="evenodd" d="M9.5 1.1l3.4 3.5.1.4v2h-1V6H8V2H3v11h4v1H2.5l-.5-.5v-12l.5-.5h6.7l.3.1zM9 2v3h2.9L9 2zm4 14h-1v-3H9v-1h3V9h1v3h3v1h-3v3z"/>
                                            </svg>
                                        </button>
                                        <button>
                                            <svg width="20px" height="20px" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg" fill=" #1e453e" stroke=" #1e453e" stroke-width="0.25">
                                                <path fill-rule="evenodd" clip-rule="evenodd" d="M14.5 2H7.71l-.85-.85L6.51 1h-5l-.5.5v11l.5.5H7v-1H1.99V6h4.49l.35-.15.86-.86H14v1.5l-.001.51h1.011V2.5L14.5 2zm-.51 2h-6.5l-.35.15-.86.86H2v-3h4.29l.85.85.36.15H14l-.01.99zM13 16h-1v-3H9v-1h3V9h1v3h3v1h-3v3z"/>
                                            </svg>                                        
                                        </button> 
                                        <button className="Mount_GoogleDrive_button" onClick={loadFileTree} disabled={loading}> 
                                            <svg xmlns="http://www.w3.org/2000/svg" width="22px" height="22px" fill=" #1e453e" stroke=" #1e453e" stroke-width="0.15" viewBox="0 -960 960 960" className={loading ? 'loading-icon' : ''}>
                                                <path d="M480-160q-134 0-227-93t-93-227q0-134 93-227t227-93q69 0 132 28.5T720-690v-110h80v280H520v-80h168q-32-56-87.5-88T480-720q-100 0-170 70t-70 170q0 100 70 170t170 70q77 0 139-44t87-116h84q-28 106-114 173t-196 67Z"/>
                                            </svg>                                          
                                        </button>
                                    </div>
                                    <div className="Divider" />                                
                                    <div className="File_tree_container">
                                        {fileTree.length > 0 ? (
                                            fileTree.map(file => (
                                                <FileTreeItem key={file.id} file={file} />
                                            ))
                                        ) : (
                                            <div style={{ textAlign: 'center', color: '#666', padding: '20px' }}>
                                                {loading ? 'Loading files...' : 'No files found. Click "Refresh Files" to load.'}
                                            </div>
                                        )}
                                    </div>
                                </div> 
                                ): (
                                    <div className="Container_2">
                                        <button className="GoogleDrive_mount_button" onClick={() => {
                                            const popup = window.open(
                                                'http://localhost:3000/auth/google/drive',
                                                'google-drive-auth',
                                                'width=500,height=600,scrollbars=yes,resizable=yes'
                                            );
                                        }}>
                                            Mount to Google Drive
                                            <svg width="25px" height="25px" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
                                                <path d="M2 11.9556C2 8.47078 2 6.7284 2.67818 5.39739C3.27473 4.22661 4.22661 3.27473 5.39739 2.67818C6.7284 2 8.47078 2 11.9556 2H20.0444C23.5292 2 25.2716 2 26.6026 2.67818C27.7734 3.27473 28.7253 4.22661 29.3218 5.39739C30 6.7284 30 8.47078 30 11.9556V20.0444C30 23.5292 30 25.2716 29.3218 26.6026C28.7253 27.7734 27.7734 28.7253 26.6026 29.3218C25.2716 30 23.5292 30 20.0444 30H11.9556C8.47078 30 6.7284 30 5.39739 29.3218C4.22661 28.7253 3.27473 27.7734 2.67818 26.6026C2 25.2716 2 23.5292 2 20.0444V11.9556Z" fill="white"/>
                                                <path d="M16.0019 12.4507L12.541 6.34297C12.6559 6.22598 12.7881 6.14924 12.9203 6.09766C11.8998 6.43355 11.4315 7.57961 11.4315 7.57961L5.10895 18.7345C5.01999 19.0843 4.99528 19.4 5.0064 19.6781H11.9072L16.0019 12.4507Z" fill="#34A853"/>
                                                <path d="M16.002 12.4507L20.0967 19.6781H26.9975C27.0086 19.4 26.9839 19.0843 26.8949 18.7345L20.5724 7.57961C20.5724 7.57961 20.1029 6.43355 19.0835 6.09766C19.2145 6.14924 19.3479 6.22598 19.4628 6.34297L16.002 12.4507Z" fill="#FBBC05"/>
                                                <path d="M16.0019 12.4514L19.4628 6.34371C19.3479 6.22671 19.2144 6.14997 19.0835 6.09839C18.9327 6.04933 18.7709 6.01662 18.5954 6.00781H18.4125H13.5913H13.4084C13.2342 6.01536 13.0711 6.04807 12.9203 6.09839C12.7894 6.14997 12.6559 6.22671 12.541 6.34371L16.0019 12.4514Z" fill="#188038"/>
                                                <path d="M11.9082 19.6782L8.48687 25.7168C8.48687 25.7168 8.3732 25.6614 8.21875 25.5469C8.70434 25.9206 9.17633 25.9998 9.17633 25.9998H22.6134C23.3547 25.9998 23.5092 25.7168 23.5092 25.7168C23.5116 25.7155 23.5129 25.7142 23.5153 25.713L20.0965 19.6782H11.9082Z" fill="#4285F4"/>
                                                <path d="M11.9086 19.6782H5.00781C5.04241 20.4985 5.39826 20.9778 5.39826 20.9778L5.65773 21.4281C5.67627 21.4546 5.68739 21.4697 5.68739 21.4697L6.25205 22.461L7.51976 24.6676C7.55683 24.7569 7.60008 24.8386 7.6458 24.9166C7.66309 24.9431 7.67915 24.972 7.69769 24.9972C7.70263 25.0047 7.70757 25.0123 7.71252 25.0198C7.86944 25.2412 8.04489 25.4123 8.22034 25.5469C8.37479 25.6627 8.48847 25.7168 8.48847 25.7168L11.9086 19.6782Z" fill="#1967D2"/>
                                                <path d="M20.0967 19.6782H26.9974C26.9628 20.4985 26.607 20.9778 26.607 20.9778L26.3475 21.4281C26.329 21.4546 26.3179 21.4697 26.3179 21.4697L25.7532 22.461L24.4855 24.6676C24.4484 24.7569 24.4052 24.8386 24.3595 24.9166C24.3422 24.9431 24.3261 24.972 24.3076 24.9972C24.3026 25.0047 24.2977 25.0123 24.2927 25.0198C24.1358 25.2412 23.9604 25.4123 23.7849 25.5469C23.6305 25.6627 23.5168 25.7168 23.5168 25.7168L20.0967 19.6782Z" fill="#EA4335"/>
                                            </svg>
                                        </button>
                                        <button className="Dropbox_mount_button">
                                            Mount to Dropbox
                                            <svg width="25px" height="25px" viewBox="0 -19 256 256" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" preserveAspectRatio="xMidYMid">
		                                        <g fill="#0061FF">
                                                    <polygon points="63.9945638 0 0 40.7712563 63.9945638 81.5425125 128 40.7712563">
                                                    </polygon>
                                                    <polygon points="192.000442 0 128 40.7750015 192.000442 81.5500031 256.000885 40.7750015">
                                                    </polygon>
                                                    <polygon points="0 122.321259 63.9945638 163.092516 128 122.321259 63.9945638 81.5500031">
                                                    </polygon>
                                                    <polygon points="192 81.5500031 128 122.324723 192 163.099442 256 122.324723">
                                                    </polygon>
                                                    <polygon points="64 176.771256 128.005436 217.542513 192 176.771256 128.005436 136">
                                                    </polygon>
		                                        </g>
                                            </svg>
                                        </button>
                                    </div>
                                )
                            }
                            <div className="resize-handle" onMouseDown={handleResizeStart}/>
                        </div>
                )}
                    <Content />
                </>
            ) : (
                <>          
                </>
            ) 
                }

        </div>
    );
}

export default Body;