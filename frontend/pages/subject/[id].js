import { useRouter } from "next/router";
import useSWR from "swr";
import { apiGet } from "../../apiClient";

const fetcher = (path) => apiGet(path);

export default function SubjectDetail() {
  const router = useRouter();
  const { id } = router.query;

  const { data: subject, error: subjectError } = useSWR(
    id ? `/subjects/${id}` : null,
    fetcher
  );
  const { data: lessons, error: lessonsError } = useSWR(
    id ? `/lessons/?subject_id=${id}` : null,
    fetcher
  );

  if (subjectError || lessonsError)
    return <div className="bhv-error">Lỗi tải dữ liệu. Vui lòng thử lại.</div>;
  if (!subject || !lessons) return <div className="bhv-loading">Đang tải bài học...</div>;

  return (
    <>
      <div className="bhv-breadcrumb">
        <a href="/">Trang chủ</a>
        <span>/</span>
        <span>{subject.title}</span>
      </div>

      <div className="bhv-page-header-eyebrow">
        <div className="bhv-dot" />
        <span>Chủ đề học tập</span>
      </div>
      <h1 className="bhv-page-title">{subject.title}</h1>
      <p className="bhv-page-subtitle">
        {subject.description ||
          "Bé sẽ được làm quen với kiến thức qua các bài học ngắn, dễ hiểu và sinh động."}
      </p>

      <h2 className="bhv-section-title">Các bài học trong chủ đề</h2>
      {lessons.length === 0 ? (
        <div className="bhv-empty">Chủ đề này chưa có bài học nào.</div>
      ) : (
        <div className="bhv-grid">
          {lessons.map((l, index) => (
            <a key={l.id} href={`/lesson/${l.id}`} className="bhv-card">
              <div className="bhv-card-header-row">
                <h3 className="bhv-card-title">{l.title}</h3>
                <div className="bhv-card-pill">Bài #{index + 1}</div>
              </div>
              <p className="bhv-card-body">
                {l.description || "Bài học ngắn với hoạt động trực quan cho bé."}
              </p>
              <div className="bhv-card-meta">
                <span className="bhv-tag-soft">Hoạt động tương tác</span>
                <span style={{ fontSize: 11, opacity: 0.8 }}>Nhấn để xem hoạt động</span>
              </div>
            </a>
          ))}
        </div>
      )}
    </>
  );
}
