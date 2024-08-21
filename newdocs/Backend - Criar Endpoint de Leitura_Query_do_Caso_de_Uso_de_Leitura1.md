```csharp
namespace Project.Application.UseCases.Brands.GetBrandById
{
    public class GetBrandByIdQuery : IQuery<GetBrandByIdDto>
    {
        public string Id { get; }
        public string OrganizationId { get; }

        public GetBrandByIdQuery(string id, string organizationId)
        {
            Id = id;
            OrganizationId = organizationId;
        }
    }
}
```