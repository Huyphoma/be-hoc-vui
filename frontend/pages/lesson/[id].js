import { useRouter } from "next/router";
import useSWR from "swr";
import { apiGet } from "../../apiClient";

const fetcher = (path) => apiGet(path);

export default function LessonDetail() {
  const router = useRouter();
  const { id } = router.query;

  const { data: lesson, error: lessonError } = useSWR(
    id ? `/lessons/${id}` : null,
    fetcher
  );
  const { data: activities, error: activitiesError } = useSWR(
    id ? `/activities/?lesson_id=${id}` : null,
    fetcher
  );

  if (lessonError || activitiesError)
    return <div className="bhv-error">Lỗi tải dữ liệu. Vui lòng thử lại.</div>;
  if (!lesson || !activities) return <div className="bhv-loading">Đang tải hoạt động...</div>;

  return (
    <>
      <div className="bhv-breadcrumb">
        <a href="/">Trang chủ</a>
        <span>/</span>
        <a href={`/subject/${lesson.subject_id || ""}`}>Chủ đề</a>
        <span>/</span>
        <span>{lesson.title}</span>
      </div>

      <div className="bhv-page-header-eyebrow">
        <div className="bhv-dot" />
        <span>Bài học</span>
      </div>
      <h1 className="bhv-page-title">{lesson.title}</h1>
      <p className="bhv-page-subtitle">
        {lesson.description ||
          "Bé sẽ thực hiện các hoạt động ngắn để ghi nhớ kiến thức một cách tự nhiên."}
      </p>

      <h2 className="bhv-section-title">Hoạt động trong bài</h2>
      {activities.length === 0 ? (
        <div className="bhv-empty">Bài này chưa có hoạt động nào.</div>
      ) : (
        <div className="bhv-activity-list">
          {activities.map((a) => (
            <div key={a.id} className="bhv-activity-card">
              <h3 className="bhv-activity-title">{a.title}</h3>
              <p className="bhv-activity-desc">
                {a.description || "Hoạt động học tập cho bé."}
              </p>
              <div className="bhv-activity-footer">
                <span className="bhv-badge-type">
                  <span />
                  {a.activity_type === "video"
                    ? "Video học"
                    : a.activity_type === "game"
                    ? "Mini game"
                    : a.activity_type === "story"
                    ? "Câu chuyện"
                    : "Hoạt động"}
                </span>
                {a.content_url && (
                  <a
                    href={a.content_url}
                    target="_blank"
                    rel="noreferrer"
                    className="bhv-link"
                  >
                    Mở nội dung
                  </a>
                )}
              </div>
            </div>
          ))}
        </div>
      )}
    </>
  );
}
