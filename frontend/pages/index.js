import useSWR from "swr";
import { apiGet } from "../apiClient";

const fetcher = (path) => apiGet(path);

export default function Home() {
  const { data: lessons } = useSWR("/api/v1/lessons/1/flow", fetcher);

  if (error) return <div className="bhv-error">Lỗi tải dữ liệu. Vui lòng thử lại.</div>;
  if (!subjects) return <div className="bhv-loading">Đang tải thế giới học tập cho bé...</div>;

  return (
    <>
      <div className="bhv-page-header-eyebrow">
        <div className="bhv-dot" />
        <span>Bé Học Vui · Dành cho phụ huynh & bé 2–7 tuổi</span>
      </div>
      <h1 className="bhv-page-title">Chọn chủ đề để bắt đầu cùng bé</h1>
      <p className="bhv-page-subtitle">
        Mỗi chủ đề là một hành trình nhỏ với video, trò chơi và câu chuyện tương tác được thiết kế
        riêng cho trẻ em Việt.
      </p>

      <div className="bhv-grid">
        {subjects.map((s, index) => (
          <a key={s.id} href={`/subject/${s.id}`} className="bhv-card">
            <div className="bhv-card-header-row">
              <h2 className="bhv-card-title">{s.title}</h2>
              <div className="bhv-card-pill">
                <span className="bhv-pill-dot" />
                Chủ đề #{index + 1}
              </div>
            </div>
            <p className="bhv-card-body">
              {s.description || "Chủ đề học tập dành cho bé."}
            </p>
            <div className="bhv-card-meta">
              <span className="bhv-tag-soft">Nội dung ngắn · Dễ hiểu</span>
              <span style={{ fontSize: 11, opacity: 0.8 }}>Nhấn để xem các bài học</span>
            </div>
          </a>
        ))}
      </div>
    </>
  );
}
